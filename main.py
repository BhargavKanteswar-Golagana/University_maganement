# python + streamit project
# motive of this project is to revise important pythons concepts
# university management system
import streamlit as st


# config the page main app
st.set_page_config(page_title="University Management System", layout="wide")
st.title("University Management Portal")
# creating a empty list of colleges 
if "colleges" not in st.session_state:
    st.session_state.colleges = []

# side bar
menu_choice = st.sidebar.radio(
    "SELECT ACTION",
    (
        "Creating College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "Display Colleges List"
    )
)
class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []
    def add_student(self, s):
        self.students.append(s)
    def add_teacher(self, t):
        self.teachers.append(t)
class person:
    def __init__(self, name,branch):
        self.name = name
        self.branch = branch
class student(person):
    def __init__(self, rollno, sname, branch):
        super().__init__(sname, branch) # call parent class constructor function and srore sname and branch in parent class
        self.rollno = rollno
class teacher(person):
    def __init__(self, tname, subject, branch):
        super().__init__(tname, branch) # call parent class constructor function and store tname and branch in parent class
        self.subject = subject

def find_college(cname):
    for c in st.session_state.colleges:
        if c.cname == cname:
            return c
    return None

if menu_choice == "Creating College":
    cname = st.text_input("Enter College Name")
    if st.button("Create College"):
        clg_obj=college(cname)  # creae a college class
        st.session_state.colleges.append(clg_obj)  # add the college object to the list of colleges
        st.success(f"{cname}")
elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please create a college first.")
    else:
        clgname = st.selectbox("choose college",[c.cname for c in st.session_state.colleges])
        rollno=st.number_input("Enter Roll Number",min_value=1,max_value=100)
        sname=st.text_input("Enter Student Name")
        branch=st.text_input("Enter Branch")
        if st.button("Add Student"):
            if not (rollno and sname and branch):
                st.error("Please fill all the fields.")
            else:
                clg_obj=find_college(clgname)
                if clg_obj:
                    stu_obj=student(rollno,sname,branch)
                    clg_obj.add_student(stu_obj)
                    st.success(f"Student {sname} added to {clgname}")
elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please create a college first.")
    else:
        clgname = st.selectbox("choose college",[c.cname for c in st.session_state.colleges])
        subject=st.text_input("Enter Subject")
        tname=st.text_input("Enter Teacher Name")
        branch=st.text_input("Enter Branch")
        if st.button("Add Teacher"):
            if not (subject and tname and branch):
                st.error("Please fill all the fields.")
            else:
                clg_obj=find_college(clgname)
                if clg_obj:
                    teach_obj=teacher(tname,subject,branch)
                    clg_obj.add_teacher(teach_obj)
                    st.success(f"Teacher {tname} added to {clgname}")
elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.info("Please create a college first.")
    else:
        clgname = st.selectbox("choose college",[c.cname for c in st.session_state.colleges])
        clg_obj=find_college(clgname)
        st.subheader(f"list of students in {clgname}")
        st.subheader("S.No : Name , Roll No , Branch")
        if clg_obj.students:
            for i, s in enumerate(clg_obj.students, start=1):
                st.write(i,":",f"Name: {s.name}, Roll No: {s.rollno}, Branch: {s.branch}")
        else:
            st.warning(f"No students found in {clgname}")
elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please create a college first.")
    else:
        clgname = st.selectbox("choose college",[c.cname for c in st.session_state.colleges])
        clg_obj=find_college(clgname)
        st.subheader(f"list of teachers in {clgname}")
        st.subheader("S.No : Name , Subject , Branch")
        if clg_obj.teachers:
            for i, t in enumerate(clg_obj.teachers, start=1):
                st.write(i,":",f"Name: {t.name}, Subject: {t.subject}, Branch: {t.branch}")
        else:
            st.warning(f"No teachers found in {clgname}")
elif menu_choice == "Display Colleges List":
    if not st.session_state.colleges:
        st.info("Please create a college first.")
    else:
        st.subheader("List of Colleges")
        for i, c in enumerate(st.session_state.colleges, start=1):
            st.write(i,":",f"{c.cname}")

            


    
    
    
