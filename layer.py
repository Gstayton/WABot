from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from yowsup.layers.protocol_presence.protocolentities import PresenceProtocolEntity
from yowsup.layers.protocol_chatstate.protocolentities.chatstate_outgoing import OutgoingChatstateProtocolEntity
from yowsup.layers.protocol_chatstate.protocolentities.chatstate import ChatstateProtocolEntity

from utilities import Urban
from helpers   import Chat

import parser

class EchoLayer(YowInterfaceLayer):
    def __init__(self, *args, **kwargs):
        super(EchoLayer, self).__init__(*args, **kwargs)

        self.Chat = parser.Chat()
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        payload = self.Chat.parse(messageProtocolEntity.getBody())
        print(payload.Type)

        if payload.Type == parser.PayloadType.CHAT_MESSAGE:
           self.toLower(Chat.createMsgEntity(
               payload.Response,
               messageProtocolEntity
               ))

        if True:
            receipt = OutgoingReceiptProtocolEntity(
                        messageProtocolEntity.getId(),
                        messageProtocolEntity.getFrom(),
                        'read',
                        messageProtocolEntity.getParticipant()
                    )

            self.toLower(receipt)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
