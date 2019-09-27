package com.englishbot;

import org.json.JSONObject;

/** Represents a chat message
 * @version 1.0
 * @author Karin Lampesberger
 */
public class Message {
    private int mType;
    private JSONObject mMessage;
    private String uniqueID;

    private Message() {}

    /**
     * Gets message type
     * @return message type
     */
    public int getType() {
        return mType;
    }

    /**
     * Gets message
     * @return message
     */
    public JSONObject getMessage() {
        return mMessage;
    };

    /**
     * Builder class for Message
     */
    public static class Builder {
        private final int mType;
        private JSONObject mMessage;
        private String uniqueID;

        public Builder(int type) {
            mType = type;
        }

        public Builder uniqueID(String uniqueID) {
            uniqueID = uniqueID;
            return this;
        }

        public Builder message(JSONObject message) {
            mMessage = message;
            return this;
        }

        /**
         * Builds message with mType, uniqueID and mMessage
         * @return message
         */
        public Message build() {
            Message message = new Message();
            message.mType = mType;
            message.uniqueID = uniqueID;
            message.mMessage = mMessage;
            return message;
        }
    }

}