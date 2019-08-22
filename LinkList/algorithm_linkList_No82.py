# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:29:48 2019

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

#删除排序链表中的重复元素(保留没有重复的结点)
def func(head):
    if head == None or head.next == None:
        return head
    dumb = ListNode(None)
    dumb.next = head
    node = dumb
    while node.next:
        tmp = node.next
        if tmp.next and tmp.next.elem == tmp.elem:
            while tmp.next and tmp.next.elem == tmp.elem:
                tmp = tmp.next
            node.next = tmp.next
        else:
            node = node.next
    return dumb.next

if __name__ == '__main__':
    L = SingleLinkList()
    n = int(input('链表长度? n = '))
    for i in range(n):
        L.append(np.random.randint(0,5))
    L.elemsSort()
    print('\n初始链表:',obtainAllElems(L.head))
    dumb = func(L.head)
    print('\n处理结果:',obtainAllElems(dumb))
                  
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
