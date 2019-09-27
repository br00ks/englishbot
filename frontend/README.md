# Frontend for EnglishBot

## Types of messages
- `Message.Type_Message` (a message sent my user)
- `Message.Type_LT_ERROR` (a received message which is LanguageTool error message)
- `Message.Type_MSG_RECEIVED` (a normal received message message)
- `Message.TYPE_GDPR_COMPLIACE` (a received message containing gdpr compliance dialogue)
- `Message.TYPE_GDPR_BUTTON` (a received message representing gdpr accept button)
- `Message.TYPE_DICTIONARY` (a received message which contains a result of a dictionary call)
- `Message.TYPE_LOADING_DOTS` (a received message to simulate typing dots -- currently not used)

Look of a message depends on its type - type is recognized either on which socket channel message is being received or depending on message structure.
