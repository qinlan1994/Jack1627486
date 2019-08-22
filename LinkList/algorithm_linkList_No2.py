# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:24:33 2019

@author: Bob
"""

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

#两数相加
def func(L1,L2):
    tag = 0
    head = ListNode(None)
    node = head
    while L1 or L2:
        a = L1.elem if L1 else 0
        b = L2.elem if L2 else 0
        s = tag + a + b
        node.next = ListNode(s%10)
        node = node.next
        tag = s // 10
        if tag == 1:
            node.next = ListNode(1)
        if L1:L1 = L1.next
        if L2:L2 = L2.next
    return head.next

if __name__ == '__main__':
    L1,L2 = SingleLinkList(),SingleLinkList()
    x = list(map(int,list(input('x = '))))
    y = list(map(int,list(input('y = '))))
    for i in x:
        L1.prepend(i)
    for j in y:
        L2.prepend(j)
    print('\nL1 =',obtainAllElems(L1.head),' L2 =',obtainAllElems(L2.head))
    head = func(L1.head,L2.head)
    s = obtainAllElems(head)
    s.reverse()
    s = ''.join([str(x)for x in s])
    print('\n求和结果: x + y = ',s)
    
    
    
        
        
        














