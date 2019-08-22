# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:13:04 2019

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
    
    def elemsSort(self):
        if self.head == None or self.head.next == None:
            return None
        node = self.head.next
        while node:
            x = node.elem
            tmp = self.head
            while tmp and tmp.elem <= x:
                tmp = tmp.next
            while tmp and tmp != node:
                y = tmp.elem
                tmp.elem = x
                x = y
                tmp = tmp.next
            node.elem = x
            node = node.next

def obtainAllElems(head):
    node = head
    elems = []
    while node:
        elems.append(node.elem)
        node = node.next
    return elems

#合并两个有序链表
def func(L1,L2):
    head = ListNode(None)
    node = head
    while L1 and L2:
        a,b = L1.elem,L2.elem
        if a < b:
            node.next = L1
            L1 = L1.next
        else:
            node.next = L2
            L2 = L2.next
        node = node.next
    node.next = L1 or L2
    return head.next

if __name__ == '__main__':
    L1,L2 = SingleLinkList(),SingleLinkList()
    m,n = list(map(int,input('输入两个链表的长度？').split(' ')))
    for i in range(m):
        L1.append(np.random.randint(0,10))
    L1.elemsSort()
    for j in range(n):
        L2.append(np.random.randint(0,10))
    L2.elemsSort()
    print('\nL1 =',obtainAllElems(L1.head),' L2 =',obtainAllElems(L2.head))
    head = func(L1.head,L2.head)
    print('\n处理结果:',obtainAllElems(head))
        
        









