# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:20:22 2019

@author: Bob
"""

import numpy as np

'''
单链表基本操作
时间复杂度 = O(1):
    -创建空表
    -判断表是否为空
    -删除表
    -首端加入/删除元素
时间复杂度 = O(n):
    -求取表长度
    -尾端加入/删除元素
    -定位加入/删除元素
    -反转表元素
时间复杂度 = nlogn:
    -排序
    

'''
class ListNode(object):
    def __init__(self,elem,link=None):
        self.elem = elem
        self.next = link

class SingleLinkList(object):
    def __init__(self):
        self.head = None
    
    def obtainAllElems(self):
        node = self.head
        elems = []
        while node:
            elems.append(node.elem)
            node = node.next
        return elems
    
    def obtainListLen(self):
        n = 0
        node = self.head
        while node:
            n += 1
            node = node.next
        return n
    
    def prepend(self,elem):
        self.head = ListNode(elem,self.head)
    def append(self,elem):
        if self.head == None:
            self.head = ListNode(elem)
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
    
    def popLeft(self):
        if self.head == None:
            print('链表已为空')
            return None
        e = self.head.elem
        self.head = self.head.next
        return e
    def popRight(self):
        if self.head == None:
            print('链表已为空')
            return None
        node = self.head
        if node.next == None:
            e = node.elem
            self.head = None
        else:
            while node.next.next:
                node = node.next
            e = node.next.elem
            node.next = node.next.next
        return e
    def targetPop(self,i):
        n = self.obtainListLen()
        if i == 1:self.popLeft()
        elif i == n:self.popRight()
        else:
            node = self.head
            while node.next.next and i > 2:
                node = node.next
                i -= 1
            e = node.next.elem
            node.next = node.next.next
            return e
    
    def elemsSort(self):
        if self.head == None or self.head.next == None:
            return None
        crt = self.head.next
        while crt:
            x = crt.elem
            node = self.head
            while node and node.elem <= x:
                node = node.next
            while node and node != crt:
                y = node.elem
                node.elem = x
                x = y
                node = node.next
            crt.elem = x
            crt = crt.next
    
    def elemsReverse(self):
        dumb = None
        while self.head:
            node = self.head
            self.head = node.next
            node.next = dumb
            dumb = node
        self.head = dumb
        
            
if __name__ == '__main__':
    L = SingleLinkList()
    print('初始链表:',L.obtainAllElems())
    
    for i in range(3):
        e = np.random.randint(0,10)
        L.prepend(e)
        print('第{}次前端插入:'.format(i+1),L.obtainAllElems())
    for i in range(3):
        e = np.random.randint(0,10)
        L.append(e)
        print('第{}次尾端插入:'.format(i+1),L.obtainAllElems())
    L.targetInsert(0,1)
    print('指定插入:i=0,e=1 ==>',L.obtainAllElems())
    L.targetInsert(4,2)
    print('指定插入:i=4,e=2 ==>',L.obtainAllElems())
    L.targetInsert(8,4)
    print('指定插入:i=8,e=4 ==>',L.obtainAllElems())
    
    L.elemsSort()
    print('排序:',L.obtainAllElems())
    L.elemsReverse()
    print('倒序:',L.obtainAllElems())
    
    L.targetPop(1)
    print('指定删除:i=1 ==>',L.obtainAllElems())
    L.targetPop(3)
    print('指定删除:i=3 ==>',L.obtainAllElems())
    L.targetPop(7)
    print('指定删除:i=7 ==>',L.obtainAllElems())
    for i in range(3):
        L.popLeft()
        print('第{}次前端删除:'.format(i+1),L.obtainAllElems())
    for i in range(3):
        L.popRight()
        print('第{}次尾端删除:'.format(i+1),L.obtainAllElems())
    
    
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            
