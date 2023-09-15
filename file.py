# ===============================Table Sql Data View==========================
        
        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=100,width=720,height=400)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Dep","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="Emp-ID")
        self.attendanceReport_left.heading("Dep",text="Department")
        self.attendanceReport_left.heading("Name",text="Emp-Name")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend-status")
        
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("ID",width=100)
        self.attendanceReport_left.column("Dep",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=500,width=720,height=60)

        #Improt button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        update_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)
