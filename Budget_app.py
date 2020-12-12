#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:39:22 2020

@author: sithlord-dev
"""

# =============================================================================
# Class
# =============================================================================
import math
class Category:
    def __init__(self,name):
        self.ledger=[]
        self.category=name
        self.balance=0
    
    def check_funds(self,check):
        if check <= self.balance:
            return True
        else :
            return False
    
    def deposit(self,dep,desc='') :
        self.balance = self.balance + dep
        self.ledger.append({"amount": dep, "description": desc})
        
    def withdraw(self,wit,desc='') :
        if self.check_funds(wit) :
            self.ledger.append({"amount": -wit, "description": desc})
            self.balance = self.balance - wit
            return True
        else :
            return False
    def get_balance(self):
        return print(self.balance)
        
    def transfer(self,tran,cat):
        trans_to_desc="Transfer to  "+ cat.category
        trans_from_desc="Transfer from  "+self.category
        if self.withdraw(tran,trans_to_desc) :
            cat.deposit(tran,trans_from_desc)
            return True
        else :
            return False
    def __str__(self):
        res = '*'*(((30-len(self.category))//2)) + self.category
        res = res + '*'*(30-(len(res)))
        for el in self.ledger :
            if float(el["amount"]) >= 10000 :
                amm = 9999.99
            else :
                amm = float(el["amount"])
            desc = el["description"][:23]
            line= desc.ljust(23) + f"{amm:.2f}".rjust(7)
            res = res + '\n' + line
            total="Total: "+ f"{self.balance:.2f}"
        res = res + '\n' + total
        return res

# =============================================================================
# Spend chart function
# =============================================================================

def create_spend_chart(categories):
    wits=dict()
    names=list()
    for cat in categories:
        names.append(cat.category)
        for el in cat.ledger :
            if float(el['amount']) < 0 :
                wit_rd = -float(el['amount'])
                #wit_rd = int(round(-float(el['amount']),-1))
                #wit_rd = int(math.floor(-float(el['amount']) / 10.0)) * 10 - 10
                wits[cat.category]=wits.get(cat.category, 0)+ wit_rd
            else :
                wits[cat.category]=0   
    res="Percentage spent by category"
    i=100
    j=0
    l= len(max(names, key=len))+1
    while i >= -l*10 :
        if i >= 0 :
            res = res + '\n' + str(i).rjust(3) + "|" +" "
            for v,k in wits.items():
                Perc = k / (sum([ k for v,k in wits.items() ] )) * 100
                if Perc < 10 :
                    n=0
                else :
                    n = int(math.floor(Perc / 10.0)) * 10
                if n >= i :
                    res = res + 'o  '
                else :
                    res = res + "   "
            i=i-10
        elif i == -10 :
            res=res+'\n'+'    '+(len(names)*"---")
            i=i-10
        else :
            res=res+'\n'+'   '
            for name in names:
                if len(name) > 0 :
                    try:
                        res = res+'  '+name[j]
                    except:
                        res = res+"   "
                else :
                    res = res+ "   "
            j=j+1
            i=i-10
    return print(res)