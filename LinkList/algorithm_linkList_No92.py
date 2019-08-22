# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:29:53 2019

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

#反转链表部分元素
'''
思路：找到指定的区域，基于前插法旋转元素；
     拼接三部分(旋转前区域+旋转区域+旋转
     后区域) 
'''
def func(head,m,n):
    dumb = ListNode(None)
    dumb.next = head
    former,node = dumb,head
    i = 1
    while i < m:
        former = node
        node = node.next
        i = i + 1
    start,end = ListNode(None),node
    while i <= n:
        tmp = node
        node = node.next
        tmp.next = start.next
        start.next = tmp
        i = i + 1
    former.next = start.next
    end.next = node
    return dumb.next

if __name__ == '__main__':
    L = SingleLinkList()
    for i in range(8):
        L.append(np.random.randint(0,10))
    print('\n初始链表:',obtainAllElems(L.head))
    m,n = list(map(int,input('起始位置? ').split(' ')))
    dumb = func(L.head,m,n)
    print('\n处理结果:',obtainAllElems(dumb))




















