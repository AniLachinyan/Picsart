from typing import List
from user import User
from user import Conversation
from abc import ABC,abstractmethod
from user import Message
import datetime



class User:
    def __init__(self,name: str, contact_info : str, conversations:List[Conversation]):
        self.setName(name)
        self.setContactInfo(contact_info)
        self.setConversations(conversations)

    def setName(self,name):
        if (isinstance(name,str) and name!=""):
            self.__name=name
        else:
            print("Please enter valid name")

    def getName(self):
        return self.__name


    def setContactInfo(self,contact_info):            
        if (isinstance(contact_info,str) and contact_info!=""):
            self.__contact_info=contact_info
        else:
            print("Please enter valid contact info")

    def getContactInfo(self):
        return self.__contact_info


    def setConversations(self, conversations):
        if(isinstance(conversations,List) and len(conversations)!=0):
            self.__conversations=conversations
        else:
            print("Please enter valid conversations") 

    def getConverstions(self):
        return self.__conversations


    def create_conversations(self, user : User)-> Conversation:
        conversation=Conversation([self,user],[self.__conversations,user.__conversations])
        self.__conversations.append(conversation)
        user.__conversations.append(conversation)
        
        return conversation
    

    def send_message(self, message: Message,conversation : Conversation)->None:
        conversation.add_message(self,message)


    def receive_message(self, message : Message, )->None:
        return message

    def manage_settings(self)->None:
        pass


    def get_conversation(self)->List[Conversation]:
        return self.get_conversation
    




class Conversation:
    def __init__(self,participants: List[User], message_history : List[Message]):
        self.setParticipants(participants)
        self.setMessageHistory(message_history)


    def setParticipants(self,participants):
        if ( isinstance (participants, List[User] )  and  len(participants) != 0):
            self.__participants=participants
        else:
            print("Please enter valid list of participants")


    def getParticipants(self,participants):
        return self.__participants


    def setMessageHistory(self,message_history):
        if ( isinstance(message_history,List[Message]) and len(message_history!=0 )):
            self.__message_history=message_history
        else:
            print("Please enter valid history list") 

    def add_message(self, message : Message)->None:
        self.__message_history.append(message)


    def add_user(self, user : User)->None:
        self.__participants.append(user)

    def get_messages(self)->List[Message]:
        return self.__message_history        




class Message(ABC):
    def __init__(self, sender : User, conversation : Conversation, timestamp: datetime):
        self.setSender=sender
        self.setConversation=conversation
        self.setTimestamp=timestamp



    def setSender(self,sender):
        if(isinstance(sender,User)):
            self.__sender=sender
        else:
            print("Please enter valid sender")


    def setConversation(self,conversation):
        if (isinstance(conversation,Conversation)):
            self.__conversation=conversation
        else:
            print("Please enter valid conversation") 



    def setTimestamp(self,timestamp):
        if (isinstance(timestamp,datetime)):
            self.__timestamp=timestamp
        else:
            print("Please enter valid time ")


    def getSender(self):
        return self.__sender

    def getConversation(self):
        return self.__conversation

    def getTimestamp(self):
        return self.__timestamp
    

    @abstractmethod
    def display_content(self)->None:
        ...

    @abstractmethod
    def get_message_type(self)->str:
        ...


class TextMessage(Message):

    def __init__(self,sender : User, conversation : Conversation, timestamp: datetime,content : str):
        super().__init__(sender,conversation,timestamp)
        self.setContent(content)


    def setContent(self,content):
        if (isinstance(content,str) and content!=""):
            self.__content=content
        else:
            print("Please enter valid content")

    def getContent(self):
        return self.__content
    

    def display_content(self) -> None:
        return self.__conversation
    
    def get_message_type(self) ->str:
        if self.__content.isdigit():
            return "integer"
        return "string"
    
class MultimediaMessage(Message):
    def __init__(self, sender: User, conversation: Conversation, timestamp: datetime, file_path : str, media_type : str):
        super().__init__(sender, conversation, timestamp)
        self.setFilePath=file_path
        self.setMediaType=media_type



    def setFilePath(self,file_path):
        if (isinstance(file_path,str) and file_path!=""):
            self.__file_path=file_path
        else:
            print("Please enter valid path")

    def getFilePath(self):
        return self.__file_path

    def setMediaType(self,media_type):
        if (isinstance(media_type,str)):
            self.__media_type=media_type
        else:
            print("Please enter valid media type")

    def getMediaType(self):
        return self.__media_type


    def display_content(self) -> None:
        print(self.__conversation)

    def get_message_type(self) -> str:
        return self.__media_type       
            



class MessagingManager(ABC):
    
    @abstractmethod
    def send_message(self, message : Message)->None:
        ...
    
    @abstractmethod
    def receive_message(self,message : Message)->None:
        ...

    @abstractmethod
    def view_conversation_history(self,conversation : Conversation)->List[Message]:
        ...








