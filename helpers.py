from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from yowsup.layers.protocol_presence.protocolentities import PresenceProtocolEntity
from yowsup.layers.protocol_chatstate.protocolentities.chatstate_outgoing import OutgoingChatstateProtocolEntity
from yowsup.layers.protocol_chatstate.protocolentities.chatstate import ChatstateProtocolEntity

class Chat():
    def createMsgEntity(msg, msgProtocolEntity):
        return TextMessageProtocolEntity(
                msg,
                to = msgProtocolEntity.getFrom()
                )

