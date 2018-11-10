#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, bs4

class MainParams():
    '''Ну короче типо тут всякие парпметры вроде деревьев элементов, массивов разных и прочей хуиты, котороую будем заимствовать'''
    def __init__(self, url):
        self.url=url
        self.get_url=requests.get(url)
        self.get_page=bs4.BeautifulSoup(self.get_url.text, "html.parser")
        self.nameElem=self.get_page.select('.hl-tr td.vf-col-t-title.tt .torTopic a')
        self.dateElem=self.get_page.select('.hl-tr td.vf-col-last-post.tCenter.small.nowrap p')
        self.lenNameElemArray=len(self.nameElem)-1
        self.lenDateElemArray=len(self.dateElem)
        self.nameElemList=[]
        self.preListDateElem=[]
        self.dateElemList=[]
        self.lenListOfname=[]
        self.dot='.'    

class Main():  
    '''Логика программы'''
    def dateCounter(self, p):
        """ Структурируемы даты """
        for i in range(p.lenDateElemArray):
            p.preListDateElem.append(p.dateElem[i].getText())
        fa=0
        for i in p.preListDateElem:
            if fa%2==0:
                p.dateElemList.append(p.preListDateElem[fa])
                fa+=1
            else:
                fa+=1
                continue
        for i in range(4):    
            p.dateElemList.pop(0)            
        return p.dateElemList
    
    def textCounter(self, p):
        """ Структурируем названия """
        for i in range(p.lenNameElemArray):
            p.nameElemList.append(p.nameElem[i].getText())
        
        for i in range(4):    
            p.nameElemList.pop(0)
        return p.nameElemList
    
    def structure(self, p):
        for i in p.nameElemList:
            p.lenListOfname.append(len(i))
        maxLen=max(p.lenListOfname)
        return maxLen
        
    def spases(self, maxLen, p):
        colspa=[]
        for i in p.nameElemList:
            colspa.append((maxLen-len(i))*p.dot)
        
        return colspa
    
    def printAll(self, maxLen, namEl, datEl, colSpa):
        h=1
        for i in namEl:
            if h<10:
                print('',h,'.   ',i, ' ', colSpa[h-1], datEl[h-1])
                h+=1
            else:
                print(h,'.   ',i, ' ', colSpa[h-1], datEl[h-1])
                h+=1                


url='https://rutracker.org/forum/viewforum.php?f=635'
f=MainParams(url)
g=Main()


def RutreckerHot(g, f):
    namEl=g.textCounter(f)
    datEl=g.dateCounter(f)
    maxLen=g.structure(f)
    colSpa=g.spases(maxLen, f)
    g.printAll(maxLen, namEl, datEl, colSpa)

RutreckerHot(g, f)
