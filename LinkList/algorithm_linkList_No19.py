# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:46:29 2019

@author: bob
"""
import numpy as np

class ListNode(object):
    def __init__(self,elem,link=None):
        self.elem = elem
        self.next = link

class SingleLinkList(object):
    def __init__(self):
        self.head = None
    
    def prepend(self,elem):
        self.head = ListNode(elem,self.head)
    def append(self,elem):
        if self.head == None:
            self.head = ListNode(elem)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = ListNode(elem)
    def targetInsert(self,i,e):
        n = self.obtainListLen()
        if i == 0:self.prepend(e)
        elif i == n:self.append(e)
        else:
            node = self.head
            while node and i > 1:
                node = node.next
                i -= 1
            p = ListNode(e)
            p.next = node.next
            node.next = p

def obtainAllElems(head):
    node = head
    elems = []
    while node:
        elems.append(node.elem)
        node = node.next
    return elems

#删除链表倒数第N个节点
'''
解题思路：使用快慢指针
        快指针从哑链表首端移到待删除元素位置，然后慢指针从头移动，当快指针移动到尾端时，
        慢指针移动到待删除元素之前的位置
'''
def func(head,n):
    dumb = ListNode(None)
    dumb.next = head
    fast = dumb
    while n:
        fast = fast.next
        n = n - 1
    slow = dumb
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dumb.next

if __name__ == '__main__':
    L = SingleLinkList()
    for i in range(8):
        L.append(np.random.randint(0,10))
    print('初始链表:',obtainAllElems(L.head))
    
    n = int(input('删除倒数第N个元素? N = '))
    dumb = func(L.head,n)
    print('\n处理结果:',obtainAllElems(dumb))
    
    
    









