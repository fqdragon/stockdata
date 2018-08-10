#!/usr/bin/python
#-*- coding: utf8 -*-
import sqlite3

class sqlite():
    def __init__(self,file):
        if file:
            self.conn = sqlite3.connect(file)
        else:
            self.conn = sqlite3.connect("E:\Develop\qz\stockdata\stockdata.sqlite")
      
    def Execute(self, sqlstr,closeflag=False):
        try:
            self.cur = self.conn.cursor()
            ret = self.cur.execute(sqlstr)
            if sqlstr.find("INSERT") != -1 or  sqlstr.find("UPDATE") != -1 or  sqlstr.find("DELETE") != -1:
                self.conn.commit()   
            self.cur.close()
            if closeflag:            
                self.conn.close()
            return ret
        except Exception as e:
            print(str(e))
            return False
      
        
    def SelectAll(self, table, closeflag = False):
        try:
            self.cur = self.conn.cursor()
            ret = self.cur.execute("select * from %s "%table)
            select_value = self.cur.fetchmany(ret)
            self.cur.close()
            
            if closeflag:            
                self.conn.close()
                
            return select_value
        except Exception as e:
            print(str(e))
            return False
        
    def SelectCondition(self, table,condition, closeflag = False):
        try:
            self.cur = self.conn.cursor()
            ret = self.cur.execute("select * from %s where %s"%(table,condition))
            select_value = self.cur.fetchmany(ret)
            self.cur.close()
            
            if closeflag:            
                self.conn.close()
                
            return select_value
        except Exception as e:
            print(str(e))
            return False

    def SelectValueCondition(self, valuename,table,condition, closeflag = False):
        try:
            self.cur = self.conn.cursor()
            ret = self.cur.execute("select %s from %s where %s"%(valuename,table,condition))
            select_value = self.cur.fetchmany(ret)
            self.cur.close()
            
            if closeflag:            
                self.conn.close()
                
            return select_value
        except Exception as e:
            print(str(e))
            return False

        
    def Close(self):
        try:
            self.cur.close()
            self.conn.close()
            return True
        except Exception as e:
            print(str(e))
            return False