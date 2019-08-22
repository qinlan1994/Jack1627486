# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:11:04 2019

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

#旋转链表
'''
思路：首先确定链表长度，并形成循环链表；
     根据链表长度和旋转次数，找到最终
     链表的首尾结点；最后将尾结点断开
     即可
'''

def func(head,k):
    n = 1
    dumb = None
    node = head
    while node.next:
        node = node.next
        n = n + 1
    node.next = head
    s = n - k%n
    tmp = node
    for i in range(s):
        tmp = tmp.next
    dumb = tmp.next
    tmp.next = None
    return dumb

if __name__ == '__main__':
    L = SingleLinkList()
    n = int(input('链表长度? n = '))
    for i in range(n):
        L.append(np.random.randint(0,10))
    print('\n初始链表:',obtainAllElems(L.head))
    k = int(input('旋转次数? k = '))
    dumb = func(L.head,k)
    print('\n处理结果:',obtainAllElems(dumb))
    
    
    


















