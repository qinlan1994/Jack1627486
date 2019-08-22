# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:15:38 2019

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

#分隔链表
def func(head,x):
    if head == None or head.next == None:
        return head
    less,more = ListNode(None),ListNode(None)
    tl,tm = less,more
    node = head
    while node:
        v = node.elem
        if v < x:
            tl.next = node
            tl = tl.next
        else:
            tm.next = node
            tm = tm.next
        node = node.next
    tl.next = more.next
    return less.next

if __name__ == '__main__':
    L = SingleLinkList()
    n = int(input('链表长度? n = '))
    for i in range(n):
        L.append(np.random.randint(0,10))
    print('\n初始链表:',obtainAllElems(L.head))
    x = int(input('分界点? x = '))
    dumb = func(L.head,x)
    print('\n处理结果:',obtainAllElems(dumb))





















