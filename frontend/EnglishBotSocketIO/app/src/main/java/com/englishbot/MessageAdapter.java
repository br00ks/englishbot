package com.englishbot;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import java.util.List;
import android.support.v7.widget.RecyclerView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/** Represents a message adapter for chat messages
 * @version 1.0
 * @author Karin Lampesberger
 */
public class MessageAdapter extends RecyclerView.Adapter<MessageAdapter.ViewHolder> {
    // list of messages
    private List<Message> mMessages;

    /**
     * Constructor for MessageAdapter
     * @param context context
     * @param messages list of messages
     */
    public MessageAdapter(Context context, List<Message> messages) {
        // set list of messages
        mMessages = messages;
    }

    /**
     * Inflates layout depending on message type
     * @param parent Parent ViewGroup
     * @param viewType integer value for view type
     * @return view Holder
     */
    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        int layout = -1;
        switch (viewType) {
            case MessageType.TYPE_MESSAGE:
                layout = R.layout.item_message_sent;
                break;
            case MessageType.TYPE_LT_ERROR:
                layout = R.layout.item_message_lterror_received;
                break;
            case MessageType.TYPE_MSG_RECEIVED:
                layout = R.layout.item_message_received;
                break;
            case MessageType.TYPE_GDPR_COMPLIANCE:
                layout = R.layout.item_message_gdpr;
                break;
            case MessageType.TYPE_GDPR_BUTTON:
                layout = R.layout.item_message_gdpr_button;
                break;
            case MessageType.TYPE_DICTIONARY:
                layout = R.layout.item_message_dictionary;
                break;
        }

        View v = LayoutInflater
                .from(parent.getContext())
                .inflate(layout, parent, false);
        return new ViewHolder(v, viewType);
    }

    /**
     *
     * @param viewHolder View holder
     * @param position integer value with position
     */
    @Override
    public void onBindViewHolder(final ViewHolder viewHolder, int position) {
        Message message = mMessages.get(position);
        final JSONObject msg_obj = message.getMessage();
        viewHolder.setMessage(msg_obj);
    }

    /**
     * Gets total number of messages
     * @return number of messages
     */
    @Override
    public int getItemCount() {
        return mMessages.size();
    }

    /**
     * Gets type for message on specific position
     * @param position position to get message type for
     * @return message type (int)
     */
    @Override
    public int getItemViewType(int position) {
        return mMessages.get(position).getType();
    }

    /**
     * Class that represents one message
     */
    public class ViewHolder extends RecyclerView.ViewHolder {
        private TextView mMessageBody;
        private TextView mMessageTitle;
        private TextView mMessageSynonyms;
        private int viewType;

        public ViewHolder(View itemView, int viewType) {
            super(itemView);
            mMessageBody = itemView.findViewById(R.id.message_body);
            mMessageTitle = itemView.findViewById(R.id.message_title);
            mMessageSynonyms = itemView.findViewById(R.id.message_synonym);
            this.viewType = viewType;
        }

        /**
         * Sets message and its elements depending on message type
         * @param message
         */
        public void setMessage(JSONObject message) {
            // if message type is dictionary message
            if (this.viewType == 5) {
                if (null == mMessageBody) return;
                String pos = "";
                String word = "";
                String definition = "";
                try {
                    pos = (String) message.get("pos");
                    word = (String) message.get("word");
                    definition = (String) message.get("definition");
                    String title = "";
                    if (pos.equals("Verb")) {
                        definition = "to " + definition;
                        title = pos.substring(0, 1).toUpperCase() + pos.substring(1) + ": to " + word;
                    } else {
                        title = pos.substring(0, 1).toUpperCase() + pos.substring(1) + ": " + word;
                    }
                    JSONArray synonyms = (JSONArray) message.get("synonyms");
                    if (synonyms != null && synonyms.length() >= 1) {
                        mMessageSynonyms.setText("Synonyms: " + synonyms.toString());
                    } else {
                        mMessageSynonyms.setText("Synonyms: -");
                    }
                    mMessageBody.setText(definition);
                    mMessageTitle.setText(title);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

            } else {
                if (null == mMessageBody) return;
                String msg = "";
                try {
                    msg = (String) message.get("message");
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                mMessageBody.setText(msg);
            }
        }

    }
}
