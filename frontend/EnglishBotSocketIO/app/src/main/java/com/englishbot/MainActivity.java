package com.englishbot;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v4.view.GravityCompat;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.util.Log;
import android.view.MenuItem;
import android.support.design.widget.NavigationView;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import com.github.nkzawa.emitter.Emitter;
import com.github.nkzawa.socketio.client.IO;
import com.github.nkzawa.socketio.client.Socket;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/**
 * Main Activity for EnglishBot
 * Handles socket channel
 * @author Karin Lampesberger
 * @version 1.0
 */
public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    private String uniqueID;
    private Socket mSocket;
    private EditText textField;
    private List<Message> messages = new ArrayList<>();
    private RecyclerView messageListView;
    private MessageAdapter messageAdapter;

    /**
     * First triggered method after Android App was launched
     * Set everything related to view
     * @param savedInstanceState Bundle instance of Activity
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textField = findViewById(R.id.edit_text);

        messageAdapter = new MessageAdapter(this, messages);
        messageListView = findViewById(R.id.messages_view);
        messageListView.setLayoutManager(new LinearLayoutManager(this));
        messageListView.setAdapter(messageAdapter);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
        navigationView.setNavigationItemSelectedListener(this);

        ImageButton sendButton = findViewById(R.id.send_msg_button);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                attemptSend();
            }
        });

    }

    /**
     * Called when view is attached to window
     * Initiates GDPR dialogue if it is the first start
     * Otherwise socket connection is being established
     */
    @Override
    public void onAttachedToWindow() {
        super.onAttachedToWindow();
        //Toast.makeText(this, "Hi UI is fully loaded", Toast.LENGTH_SHORT).show();
        // steps for getting uuid and name
        SharedPreferences sharedPreferences = this.getSharedPreferences( "com.englishbot.preferences", MODE_PRIVATE);
        uniqueID = sharedPreferences.getString("uniqueId", null);

        // create and save uniqueID if it hasn't been created yet
        if (uniqueID == null) {
            SharedPreferences.Editor editor = sharedPreferences.edit();
            uniqueID = UUID.randomUUID().toString();
            editor.putString("uniqueID", uniqueID);
            editor.apply();
        }
        // set and store gdprPref flag
        boolean gdprPref = sharedPreferences.getBoolean("gdpr_accepted", false);
        if (!gdprPref) {
            gdprDialog();
        } else {
            // establish socket connection when gdpr accepted
            createSocketConnection();
        }
    }

    /**
     *
     * @param v View
     */
    public void acceptGDPR(View v) {
        SharedPreferences sharedPreferences = this.getSharedPreferences(
                getString(R.string.preference_file_key), MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putBoolean("gdpr_accepted", Boolean.TRUE);
        editor.apply();
        createSocketConnection();
    }

    /**
     * Create socket connection
     */
    private void createSocketConnection() {
        {
            try {
                mSocket = IO.socket(Constants.CHAT_SERVER_URL);
            } catch (URISyntaxException ignored) {}
        }
        // define socket channels
        mSocket.on(getString(R.string.userMessage), onUserMessage);
        mSocket.on(getString(R.string.botMessage), onBotMessage);
        mSocket.on(getString(R.string.botErrorMessage), onBotErrorMessage);
        mSocket.on(getString(R.string.sessionRequest), onBotMessage);
        mSocket.on(getString(R.string.startConversation), onBotMessage);

        // establish socket connection
        mSocket.connect();
        try {
            JSONObject data = new JSONObject();
            data.put("session_id", mSocket.id());
            mSocket.emit(getString(R.string.sessionRequest),data);

        } catch (JSONException e) {
            e.printStackTrace();
        }

        try {
            JSONObject data = new JSONObject();
            data.put("session_id", mSocket.id());
            data.put("userID", uniqueID);
            data.put("gdpr_accepted", false);
            data.put("name", null);
            mSocket.emit(getString(R.string.startConversation),data);

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    /**
     * Try to send user input to server
     * use socket channel user_uttered
     */
    private void attemptSend() {
        if (null == uniqueID) return;
        if (!mSocket.connected()) return;

        // get message from text field
        String message = textField.getText().toString().trim();
        if (TextUtils.isEmpty(message)) {
            messageListView.requestFocus();
            return;
        }
        textField.setText("");
        // add message to message adapter
        addMessage(uniqueID, convertToJSONObject(message), 0);

        try {
            // create json object to send to server
            JSONObject data = new JSONObject();
            data.put("userID", uniqueID);
            data.put("message", message);
            data.put("session_id", mSocket.id());
            // perform the sending message attempt.
            mSocket.emit(getString(R.string.userMessage), data);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    /**
     *
     */
    private Emitter.Listener onUserMessage = new Emitter.Listener() {
        @Override
        public void call(final Object... args) {

            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    JSONObject data = (JSONObject) args[0];
                    String username;
                    String message;
                    int msgType;
                    try {
                        username = (String) data.get("username");
                        message = (String) data.get("reply");
                        msgType = 0;
                    } catch (JSONException e) {
                        // Log.e(TAG, e.getMessage());
                        return;
                    }
                    addMessage(username, convertToJSONObject(message), msgType);
                }
            });
        }
    };

    /**
     *
     */
    private Emitter.Listener onBotMessage = new Emitter.Listener() {
        @Override
        public void call(final Object... args) {

            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    JSONObject data = (JSONObject) args[0];
                    String message;
                    int msgType;
                    try {
                        message = (String) data.get("text");
                        msgType = 2;
                    } catch (JSONException e) {
                        // Log.e(TAG, e.getMessage());
                        return;
                    }
                    // something else than a regular message has been sent!
                    if (message.startsWith("[{")) {
                        JSONArray results = null;
                        JSONArray definitions;
                        try {
                            results = new JSONArray(message);

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        try {
                            assert results != null;
                            definitions = results.getJSONObject(0).getJSONArray("results");
                            for (int i = 0; i < definitions.length(); i++) {
                                JSONObject tmp_obj = definitions.getJSONObject(i);
                                addMessage("", tmp_obj, 5);
                                }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        // else it's a normal message
                    } else {
                        addMessage("", convertToJSONObject(message), msgType);
                    }
                }
            });
        }
    };

    // language tool error received
    /**
     *
     */
    private Emitter.Listener onBotErrorMessage = new Emitter.Listener() {
        @Override
        public void call(final Object... args) {

            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    JSONObject data = (JSONObject) args[0];
                    JSONObject message_obj;
                    try {
                        JSONArray arr = data.getJSONArray("text");
                        for (int i = 0; i < arr.length(); i++) {

                            message_obj = arr.getJSONObject(i);
                            addMessage("", message_obj, 1);

                        }
                    } catch (JSONException e) {
                        Log.e("error on bot error", e.getMessage());
                    }
                }
            });
        }
    };

    /**
     * Initiates scroll down to bottom of message list
     */
    private void scrollToBottom() {
        messageListView.scrollToPosition(messageAdapter.getItemCount() - 1);
    }

    /**
     * Adds message to MessageAdapter
     * @param uniqueID unique application id
     * @param message user message
     * @param msgType message type
     */
    private void addMessage(String uniqueID, JSONObject message, int msgType) {
        messages.add(new Message.Builder(msgType)
                .uniqueID(uniqueID).message(message).build());
        // notify on new message
        messageAdapter.notifyItemInserted(messages.size() - 1);
        scrollToBottom();
    }

    /**
     * Function to convert given string to json object
     * @param message Message string to convert to json object
     * @return json object
     */
    private JSONObject convertToJSONObject(String message) {
        JSONObject obj = new JSONObject();
        try {
            obj.put("message", message);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return obj;
    }

    /**
     * Method to send standard GDPR dialogue on startup, if GDPR dialogue hasn't been accepted yet
     */
    public void gdprDialog() {
        JSONObject data1 = new JSONObject();
        try {
            data1.put("message", "Hello! \uD83E\uDD16 My name is EnglishBot and I am here to help you with English!");
            addMessage(uniqueID, data1, 2);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JSONObject data2 = new JSONObject();
        try {
            data2.put("message", "ℹ  To be able to communicate with me I need your approval for the use of personal " +
                    "information you may provide during our communication. Don't worry, everything will be GDPR compliant.");
            addMessage(uniqueID, data2, 2);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JSONObject data3 = new JSONObject();
        try {
            data3.put("message", "ℹ I store your personal information so we can " +
                    "pick up the conversation if we talk later. Furthermore your data will be stored in order to improve myself. Are you okay with that?");
            addMessage(uniqueID, data3, 2);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JSONObject data4 = new JSONObject();
        try {
            data4.put("message","");
            addMessage(uniqueID, data4, 4);

        } catch (JSONException e) {
            e.printStackTrace();
        }

    }
    /**
     * Standard Android method
     * Android Application life cycle
     */
    @Override
    public void onDestroy() {
        super.onDestroy();
        try {
            mSocket.disconnect();
        } catch (RuntimeException e) {
            // catch when no socket connection and application is being closed
        }
    }

    /**
     * Standard Android method
     * Android Application life cycle
     */
    @Override
    protected void onResume() {
        super.onResume();
    }

    /**
     * Android NavigationDrawer method
     */
    @Override
    public void onBackPressed() {
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }
    /**
     * Standard android navigation drawer
     * @param item MenuItem that is changed
     * @return boolean value
     */
    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_chat) {
        } else if (id == R.id.nav_learning_progress) {

        } else if (id == R.id.nav_vocabulary) {

        } else if (id == R.id.nav_settings) {

        } else if (id == R.id.nav_imprint) {

        }

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
