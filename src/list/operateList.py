from asyncio.log import logger
from email.quoprimime import header_check
import logging
from typing import List
from .creatList import ListNode
from src.common.logger import Logger


class OperateList(object):
    """"
    operate list
    """
    def __init__(self) -> None:
        self.logger = Logger("Operate List").getlogger(leavel=logging.DEBUG)\

    def createList(self, length):
        """
        create list
        """
        listnode = None
        for i in range(length,0,-1):
            listnode = ListNode(i, listnode)
        self.logger.info("Create list success !!!")
        return listnode

    def printList(self, head) -> List:
        """
        Print list
        """
        if (head == None):
            self.logger.error("List is None !!!")
            return head.val   

        list_var = [] 
        while head:
            list_var.append(head.val)
            head = head.next
        self.logger.info(f"Print list: {list_var}")

    def reverseList(self, head: ListNode) -> ListNode:
        """
        Revese list(iterate)
        """
        # if (head == None):
        #     self.logger.error("List is None !!!")
        #     return head 
        re_list = None
        while head:           
            tmp = head.next
            head.next = re_list
            re_list = head
            head = tmp
        self.logger.info(f"Revese list success !!!")
        return re_list

    def recursion_re_list(self, head: ListNode) -> ListNode:
        """
        Revese list(recursion)
        """
        if (head == None or head.next == None):
            return head
        newhead = self.recursion_re_list(head.next)
        head.next.next = head
        head.next = None
        return newhead