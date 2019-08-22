# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:56:16 2019

@author: Bob
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

def reverse(head):
    dumb = None
    while head:
        tmp = head
        head = tmp.next
        tmp.next = dumb
        dumb = tmp
    return dumb

#重排链表(L0 L1 ...Ln --> L0 Ln L1 Ln-1 ...)
'''
思路：快慢指针寻找链表中点
     反转后半段链表元素
     插空重排链表元素
'''
def func(head):
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    L1,L2 = head,reverse(slow.next)
    slow.next = None
    while L2:
        t1 = L1.next
        L1.next = L2
        t2 = L2.next
        L2.next = t1
        L1 = L1.next.next
        L2 = t2
    return head

if __name__ == '__main__':
    L = SingleLinkList()
    n = int(input('链表长度? n = '))
    for i in range(n):
        L.append(np.random.randint(0,10))
    print('\n初始链表:',obtainAllElems(L.head))
    dumb = func(L.head)
    print('\n处理结果:',obtainAllElems(dumb))
        


area = input()[1:-1]














