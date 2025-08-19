import random
import string
from datetime import datetime, timedelta


def generate_random_email():
    username_length = random.randint(5, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_chinese_name():
    chinese_surnames = [
        "Tan", "Lim", "Lee", "Ng", "Ong", "Wong", "Goh", "Chua", "Koh", "Teo", "Chan", "Yeo", "Ang", "Chong", "Leong", "Foo", "Sim", "Tay", "Ho", "Low",
        "Chen", "Lin", "Huang", "Zhang", "Li", "Wang", "Liu", "Wu", "Yang", "Zhou", "Xu", "Sun", "Ma", "Zhu", "Hu", "Guo", "He", "Gao", "Lin", "Luo",
        "Zheng", "Liang", "Xie", "Song", "Tang", "Xu", "Han", "Feng", "Deng", "Xiao", "Cheng", "Cao", "Peng", "Zeng", "Xue", "Lu", "Su", "Pan", "Jiang", "Bai",
        "Du", "Yin", "Mei", "Fang", "Fu", "Yuan", "Cai", "Jia", "Gu", "Xiong", "Hao", "Shao", "Meng", "Long", "Wei", "Wan", "Duan", "Qiu", "Jiang", "Qin",
        "Chu", "Yu", "Shen", "Qi", "Cui", "Ren", "Tian", "Xia", "Shi", "Hou", "Yan", "Jin", "Kong", "Wei", "Xiang", "Yao", "Yan", "Sheng", "Zu", "Qian"
    ]

    chinese_given_names = [
        "Wei", "Hui", "Xin", "Yi", "Ying", "Jie", "Ling", "Zhi", "Qiang", "Mei", "Jun", "Xiang", "Hao", "Chen", "Ming", "Feng", "Yang", "Cheng", "Yong", "Tian",
        "Jing", "Yan", "Fei", "Yu", "Xiuying", "Guiying", "Chunmei", "Xiaohong", "Xiulan", "Guilan", "Huifang", "Xiuzhen", "Yumei", "Xiumei", "Guirong", "Shulan", "Guizhi", "Xiuyun", "Huiying", "Jinlan",
        "Qing", "Xuan", "Zhen", "Rui", "Kai", "Sheng", "Hong", "Xiong", "Lei", "Hua", "Bin", "Heng", "Xiaowei", "Xiaojun", "Xiaofeng", "Xiaogang", "Xiaoming", "Xiaohua", "Xiaohui", "Xiaolin",
        "An", "Bao", "Bo", "Chang", "Chao", "Da", "Dong", "En", "Gang", "Guo", "Hai", "Han", "Jian", "Jiao", "Jin", "Kang", "Lang", "Li", "Liang", "Miao",
        "Nan", "Peng", "Ping", "Qi", "Qian", "Rong", "Ru", "Shan", "Shu", "Tai", "Tao", "Wen", "Wu", "Xia", "Xian", "Xiao", "Xue", "Yao", "Yi", "Yin",
        "Yu", "Yuan", "Yun", "Zhan", "Zhe", "Zhong", "Zi", "Ai", "Bi", "Cai", "Can", "Ce", "Cui", "Di", "E", "Fu", "Gai", "Gan", "Huan", "Jia",
        "Jiu", "Ju", "Kui", "Lan", "Lian", "Meng", "Nian", "Ning", "Nu", "Pin", "Qiu", "Quan", "Sha", "Shi", "Si", "Song", "Su", "Ti", "Tong", "Wai",
        "Xi", "Xiu", "Xu", "Ya", "Yan", "Ye", "Ying", "You", "Zai", "Ze", "Zeng", "Zhi", "Zhuo", "Zi", "Zong", "Zou"
    ]
    surname = random.choice(chinese_surnames)
    given_name = random.choice(chinese_given_names)
    if random.random() < 0.5:
        given_name += ' ' + random.choice(chinese_given_names)
    return f"{surname} {given_name}"


def generate_malay_name():
    malay_given_names = [
        "Abdullah", "Abdul Rahman", "Abdul Rahim", "Abdul Aziz", "Abdul Kadir", "Abdul Latif", "Abdul Malik", "Abdul Razak", "Abu Bakar", "Adam", "Adil", "Adnan", "Ahmad", "Aiman", "Aizat", "Akmal", "Ali", "Amin", "Amir", "Ammar",
        "Anuar", "Arif", "Ashraf", "Asraf", "Azhar", "Aziz", "Azlan", "Azman", "Azmi", "Badrul", "Baharudin", "Bakri", "Borhan", "Burhanuddin", "Che", "Danial", "Daud", "Dzulkifli", "Edzham", "Fadil", "Fahmi", "Faisal", "Faizal", "Farid", "Faris",
        "Fauzi", "Fuad", "Ghazali", "Hadi", "Hafiz", "Hakim", "Halim", "Hamid", "Hamzah", "Hanafi", "Haris", "Harith", "Haron", "Hasan", "Hashim", "Hassan", "Haziq", "Helmi", "Hisham", "Husain", "Hussein", "Ibrahim", "Idris", "Ihsan",
        "Imran", "Irfan", "Isa", "Ismail", "Izwan", "Jafar", "Jamal", "Jamil", "Johari", "Kamal", "Kamarul", "Kamaruzaman", "Khairil", "Khairuddin", "Khalid", "Lokman", "Lutfi", "Mahathir", "Mahmud", "Majid", "Malik", "Mansor", "Mas", "Mat", "Megat",
        "Mizan", "Mohamad", "Mohamed", "Mohammad", "Mohammed", "Mohd", "Muhamad", "Muhammad", "Muhsin", "Mukhriz", "Munir", "Mustafa", "Muthu", "Nasir", "Nasrudin", "Nazri", "Nik", "Nizam", "Noor", "Nor", "Nordin", "Omar", "Osman", "Othman",
        "Radzi", "Rafiq", "Rahimi", "Rahim", "Rahman", "Rashid", "Razak", "Razali", "Redza", "Redzuan", "Riduan", "Rizal", "Roslan", "Ruslan", "Saad", "Sabri", "Saffuan", "Saiful", "Saleh", "Salleh", "Samad", "Shafiq", "Shah", "Shahrul", "Shamsudin",
        "Shamsul", "Sharif", "Sulaiman", "Syed", "Syukri", "Tarmizi", "Taufiq", "Tengku", "Umar", "Wan", "Yusof", "Yusoff", "Yusri", "Zafran", "Zainal", "Zakaria", "Zaki", "Zamri", "Zikri", "Zulkifli",
        "Adibah", "Adila", "Adina", "Afiqah", "Aida", "Aishah", "Aisyah", "Alya", "Amalina", "Amelia", "Amira", "Amirah", "Aminah", "Anisah", "Aqilah", "Arissa", "Asma", "Asmah", "Atiqah", "Azizah",
        "Azlina", "Azwa", "Balqis", "Dalila", "Dayang", "Eliana", "Emilia", "Farah", "Farhana", "Farhanah", "Fariha", "Faridah", "Farihah", "Fasihah", "Fatimah", "Fatin", "Fazlin", "Hafizah", "Halimatun", "Hamidah",
        "Hanisah", "Hasmah", "Hasnah", "Haziqah", "Hazwani", "Hidayah", "Humaira", "Izzati", "Jamilah", "Khadijah", "Khairunnisa", "Laila", "Latifah", "Lina", "Madiha", "Maisarah", "Mariam", "Maryam", "Mas", "Mastura",
        "Mawar", "Nabila", "Nabilah", "Nadiah", "Nadirah", "Nafeesa", "Najwa", "Nasyitah", "Natasha", "Nazifah", "Nazirah", "Nik", "Noor", "Noorul", "Nor", "Nora", "Noraini", "Norashikin", "Norazlina", "Norhayati",
        "Noriah", "Norizan", "Norlia", "Normah", "Norziana", "Nur", "Nurain", "Nuraina", "Nuraliya", "Nuramira", "Nurassyifa", "Nurdiana", "Nurfadilah", "Nurfaizah", "Nurfarahana", "Nurhafizah", "Nurhaliza", "Nurhayati", "Nurhidayah", "Nurin",
        "Nurliyana", "Nurmala", "Nurshahira", "Nursyafiqah", "Nursyahirah", "Nurul", "Puteri", "Qistina", "Rabiatul", "Rabiatuladawiyah", "Radin", "Rahmah", "Raja", "Rashidah", "Rosmah", "Rossita", "Rozita", "Safiah", "Safinah", "Safiyyah",
        "Saleha", "Salina", "Salma", "Saodah", "Sarah", "Shafiqah", "Sharifah", "Siti", "Sofia", "Sofiah", "Sofiyah", "Sumaiyah", "Suraya", "Syafiqah", "Syahirah", "Syairah", "Syakila", "Syamimi", "Syaza", "Syazwani",
        "Tengku", "Ummi", "Umi", "Wan", "Yasmin", "Yusrina", "Zainab", "Zainal", "Zainun", "Zakiah", "Zaleha", "Zalina", "Zanariah", "Zarina", "Zulaika", "Zulaikha", "Zulaikhah", "Zulfah"
    ]
    malay_surnames = ["bin", "binti"]
    first_name = random.choice(malay_given_names)
    middle_name = random.choice(malay_given_names)
    surname = random.choice(malay_surnames)
    titles = ["Haji", "Hajjah", "Tan Sri", "Puan Sri", "Datuk", "Datin", "Tun", "Toh Puan"]
    if random.random() < 0.1:
        title = random.choice(titles)
        return f"{title} {first_name} {surname} {middle_name}"
    return f"{first_name} {surname} {middle_name}"


def generate_indian_name():
    indian_given_names = [
        "Aadhav", "Aadit", "Aaditya", "Aakash", "Aalam", "Aalok", "Aamir", "Aanjaneya", "Aarav", "Aarnav", "Aarush", "Aayush", "Abha", "Abhai", "Abhay", "Abhijat", "Abhijeet", "Abhimanyu", "Abhinav", "Abhishek",
        "Abishek", "Aditi", "Aditya", "Advik", "Agastya", "Agni", "Aishwarya", "Ajay", "Ajeet", "Akash", "Akhil", "Akshay", "Akshita", "Alok", "Amal", "Aman", "Amar", "Amarnath", "Amey", "Amish",
        "Amit", "Amita", "Amitabh", "Amolak", "Amrita", "Anand", "Anandi", "Anamika", "Ananth", "Ananya", "Anarya", "Anay", "Anaya", "Aniket", "Anil", "Aniruddha", "Anish", "Anit", "Anita", "Anjali",
        "Anjana", "Anjan", "Anjney", "Ankit", "Ankita", "Ankur", "Anmol", "Ansh", "Anshika", "Anshul", "Anuj", "Anupam", "Anushka", "Anurag", "Aparna", "Apoorva", "Arav", "Arjun", "Arka", "Arnav",
        "Arohi", "Arpit", "Artha", "Arun", "Aruna", "Arundhati", "Arushi", "Arya", "Asha", "Ashok", "Ashwin", "Asim", "Astha", "Atharv", "Ati", "Atiksh", "Atishay", "Atul", "Aum", "Avani",
        "Avantika", "Avichal", "Avinash", "Ayaan", "Ayush", "Ayushi", "Bala", "Balaji", "Bharat", "Bharath", "Bhargav", "Bhargavi", "Bhaskar", "Bhavana", "Bhavesh", "Bhavya", "Bhoomi", "Bijay", "Bina", "Bindu",
        "Chandan", "Chandra", "Chandran", "Charu", "Chetan", "Chetana", "Chirag", "Chitrangada", "Darshan", "Daya", "Deepa", "Deepak", "Deepika", "Dev", "Deva", "Devdan", "Devendra", "Devi", "Devika", "Dhairya",
        "Dhananjay", "Dharma", "Dharmendra", "Dhruv", "Dilip", "Disha", "Divya", "Diya", "Durga", "Esha", "Ekta", "Gauri", "Gautam", "Gayathri", "Geeta", "Girish", "Gita", "Gitanjali", "Gopal", "Gopinath",
        "Govind", "Gowri", "Gulshan", "Gunjan", "Guru", "Harsh", "Harsha", "Harshad", "Harshita", "Hema", "Hemant", "Himani", "Hira", "Hiren", "Indira", "Indra", "Indu", "Ira", "Ishan", "Isha",
        "Ishaan", "Ishani", "Ishita", "Jai", "Jatin", "Jaya", "Jayant", "Jayanti", "Jayin", "Jhanvi", "Jitendra", "Jiya", "Jyoti", "Kabir", "Kalindi", "Kalpana", "Kalyani", "Kanak", "Karan", "Karthik",
        "Kartik", "Karuna", "Kaustubh", "Kavita", "Kavya", "Keerthi", "Keshav", "Ketan", "Khushi", "Kiara", "Kiran", "Kirti", "Krishna", "Krish", "Kriti", "Kritika", "Kshitij", "Kunal", "Kushal", "Lakshmi",
        "Lalit", "Lalita", "Lavanya", "Laxmi", "Leela", "Madhav", "Madhavi", "Madhur", "Mahendra", "Mahesh", "Mahima", "Mahi", "Mallika", "Manasi", "Manish", "Manju", "Manjula", "Manoj", "Manohar", "Maya",
        "Mayank", "Meena", "Meera", "Megha", "Mehul", "Mira", "Mitali", "Mohit", "Mridula", "Mukesh", "Mukta", "Muskaan", "Nachiket", "Naman", "Namita", "Nandini", "Narayan", "Naren", "Naveen", "Navin",
        "Neela", "Neelam", "Neeti", "Neha", "Nidhi", "Nikhil", "Nikita", "Nilam", "Nilesh", "Nilima", "Nimesh", "Nirmal", "Nirmala", "Nirupama", "Nisha", "Nishant", "Nishtha", "Nitesh", "Niti", "Nitya",
        "Om", "Ojas", "Omkar", "Pankaj", "Parag", "Paras", "Parth", "Parvati", "Pooja", "Prabhat", "Prachi", "Pradip", "Pragya", "Prakash", "Pramod", "Pranav", "Praney", "Pranita", "Prasad", "Pratap",
        "Pratibha", "Pratik", "Praveen", "Prem", "Prerna", "Preeti", "Priya", "Priyanka", "Puja", "Puneet", "Purvi", "Pushpa", "Rachana", "Radha", "Radhika", "Raghu", "Rahul", "Raj", "Raja", "Rajat",
        "Rajeev", "Rajendra", "Rajesh", "Raju", "Rakesh", "Ram", "Rama", "Ramesh", "Rani", "Ranjana", "Ranjit", "Rashmi", "Ravi", "Ravindra", "Rekha", "Renuka", "Reva", "Richa", "Riddhi", "Riddhima",
        "Rishabh", "Rishi", "Rita", "Ritesh", "Ritika", "Rohan", "Rohit", "Roopa", "Ruchi", "Rudra", "Rupal", "Rupali", "Rushil", "Sachin", "Sahil", "Sakshi", "Sameer", "Samir", "Sandeep", "Sandya",
        "Sanjay", "Sanjiv", "Sankar", "Santosh", "Saras", "Sarika", "Sarthak", "Satish", "Satyam", "Saurabh", "Savar", "Seema", "Shailesh", "Shalu", "Shanta", "Shantanu", "Sharad", "Sharmila", "Shashi", "Shekhar",
        "Shilpa", "Shiva", "Shivani", "Shraddha", "Shreeya", "Shreya", "Shri", "Shriram", "Shubha", "Shubham", "Shweta", "Siddharth", "Simar", "Simran", "Smita", "Smriti", "Sneha", "Soham", "Sohini", "Sonam",
        "Sonia", "Srijan", "Srinivas", "Subhash", "Suchitra", "Sudhir", "Sujata", "Sukanya", "Suman", "Sumati", "Sumit", "Sundar", "Sundari", "Sunil", "Sunita", "Supriya", "Suraj", "Suresh", "Surya", "Sushil",
        "Sushma", "Swapna", "Swapnil", "Swati", "Tanisha", "Tanmay", "Tanuj", "Tanvi", "Tanya", "Tarun", "Tej", "Tejas", "Tejashri", "Tina", "Trisha", "Triveni", "Tuhina", "Tushar", "Udai", "Uday",
        "Ujjwal", "Uma", "Umang", "Upasana", "Urvi", "Usha", "Uttam", "Vaibhav", "Vaishnavi", "Varun", "Varsha", "Vasant", "Vasudha", "Vedant", "Vidhi", "Vidya", "Vijay", "Vimal", "Vinay", "Vineet",
        "Vinod", "Vipul", "Viraj", "Vishal", "Vishnu", "Vivek", "Yash", "Yashoda", "Yogesh", "Yuvraj"
    ]

    indian_surnames = [
        "Acharya", "Agarwal", "Aggarwal", "Ahluwalia", "Ahuja", "Arora", "Anand", "Awasthi", "Babu", "Badal", "Bajaj", "Bajwa", "Bakshi", "Balakrishnan", "Balan", "Balasubramanian", "Banerjee", "Banik", "Bansal", "Basu",
        "Batra", "Bhagat", "Bhalla", "Bhandari", "Bhardwaj", "Bhargava", "Bhasin", "Bhat", "Bhatia", "Bhatt", "Bhattacharya", "Bhavsar", "Bedi", "Bhojwani", "Bose", "Buch", "Chauhan", "Chadha", "Chakrabarti", "Chakraborty",
        "Chandra", "Chatterjee", "Chaturvedi", "Chauhan", "Chawla", "Cherian", "Chokshi", "Chopra", "Choudhary", "Choudhury", "D'Souza", "Dalmia", "Das", "Dasgupta", "Datta", "Dave", "Dayal", "Desai", "Deshmukh", "Deshpande",
        "Devan", "Dewan", "Dhar", "Dhawan", "Dhillon", "Dixit", "Doshi", "Dua", "Dube", "Dubey", "Dugar", "Dutt", "Dutta", "Dwivedi", "Fernandes", "Gandhi", "Ganesh", "Ganguly", "Garg", "George", "Ghosh", "Gokhale", "Goel",
        "Goswami", "Gour", "Goyal", "Guha", "Gulati", "Gupta", "Halder", "Handa", "Hans", "Hegde", "Hora", "Iyengar", "Iyer", "Jain", "Jaiswal", "Jani", "Jayaraman", "Jha", "Jhaveri", "Johar", "Joshi", "Kakkar", "Kala",
        "Kale", "Kalra", "Kanda", "Kannan", "Kapoor", "Kapur", "Kar", "Karnik", "Kashyap", "Kaul", "Kaur", "Khatri", "Khanna", "Khandelwal", "Kher", "Khosla", "Khurana", "Kohli", "Kochhar", "Kothari", "Krishna", "Krishnamurthy",
        "Krishnan", "Kulkarni", "Kumar", "Kumari", "Kurian", "Kuruvilla", "Lal", "Lalla", "Lamba", "Lobo", "Madhavan", "Mahajan", "Mahalingam", "Maheshwari", "Majumdar", "Malhotra", "Malik", "Manikandan", "Mani", "Manna",
        "Mathew", "Mathur", "Mehra", "Mehrotra", "Mehta", "Menon", "Mirchandani", "Mishra", "Misra", "Mistry", "Mitra", "Modi", "Mohan", "Mohanty", "Mukherjee", "Mukhopadhyay", "Nagar", "Nagarajan", "Nair", "Nambiar",
        "Nambudiripad", "Nanda", "Narang", "Narayan", "Narayanan", "Nath", "Nayak", "Nayar", "Nazareth", "Nigam", "Nimbkar", "Oak", "Om", "Padmanabhan", "Pai", "Pal", "Palan", "Pande", "Pandey", "Pandit", "Pant", "Parekh",
        "Parikh", "Patel", "Pathak", "Patil", "Patnaik", "Patra", "Pillai", "Prabhakar", "Prabhu", "Pradhan", "Prakash", "Prasad", "Prashad", "Puri", "Purohit", "Radhakrishnan", "Ragavan", "Raghavan", "Rai", "Raj", "Raja",
        "Rajan", "Rajagopalan", "Raju", "Ram", "Rama", "Raman", "Ramanathan", "Ramaswamy", "Ramachandran", "Ramakrishnan", "Rangan", "Ranganathan", "Rao", "Rastogi", "Ratta", "Rattan", "Ratti", "Rau", "Raval", "Ravindran",
        "Ray", "Reddy", "Roy", "Sabharwal", "Sachdev", "Sachdeva", "Sagar", "Saha", "Sahni", "Saini", "Salvi", "Samarth", "Sampath", "Sampat", "Samuel", "Sandhu", "Sane", "Sanghi", "Sanghvi", "Sankar", "Sankaran", "Sant",
        "Saraf", "Sarin", "Sarkar", "Sarma", "Sarna", "Sastry", "Sathe", "Savant", "Sawhney", "Saxena", "Sebastian", "Sehgal", "Sen", "Sengupta", "Sequeira", "Seth", "Sethi", "Setty", "Shah", "Shankar", "Sharma", "Shenoy",
        "Sheth", "Shetty", "Shroff", "Shukla", "Sinha", "Sodhi", "Solanki", "Som", "Soman", "Somani", "Soni", "Sood", "Sridhar", "Srinivas", "Srinivasan", "Srivastava", "Subramaniam", "Subramanian", "Sundaram", "Sur", "Suri",
        "Swaminathan", "Swamy", "Tagore", "Talwar", "Tandon", "Tata", "Tella", "Thakkar", "Thakur", "Thomas", "Tiwari", "Trivedi", "Upadhyay", "Upadhyaya", "Vaidya", "Varghese", "Varkey", "Varma", "Varman", "Vasa", "Venkataraman",
        "Venkatesh", "Verma", "Vijayakumar", "Virk", "Viswanathan", "Vohra", "Vora", "Vyas", "Wable", "Wadhwa", "Wagle", "Wahi", "Walia", "Walla", "Warrior", "Wason", "Yadav", "Yogi", "Zaveri", "Zachariah"
    ]
    given_name = random.choice(indian_given_names)
    surname = random.choice(indian_surnames)
    return f"{given_name} {surname}"


def generate_name():
    name_generators = [generate_chinese_name, generate_malay_name, generate_indian_name]
    chosen_generator = random.choice(name_generators)
    return chosen_generator(), chosen_generator


def generate_nric():
    digits = ''.join(random.choices(string.digits, k=8))
    checksum = random.choice(string.ascii_uppercase)
    return f"S{digits}{checksum}"


def generate_phone_number():
    return f"+65 {random.randint(8000, 9999)} {random.randint(1000, 9999)}"


def generate_drivers_license():
    return f"S{random.randint(1000000, 9999999):07d}{random.choice(string.ascii_uppercase)}"


def generate_cpf_number():
    return f"S{random.randint(1000000, 9999999):07d}{random.choice(string.ascii_uppercase)}"


def calculate_age(dob):
    today = datetime.now()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def generate_passport_number():
    return f"K{random.randint(1000000, 9999999)}{random.choice(string.ascii_uppercase)}"


def generate_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)


def generate_profile():
    countries = ["Singapore", "Malaysia", "China", "India", "Indonesia", "Philippines", "Vietnam", "Thailand", "Myanmar", "Cambodia", "Laos", "Brunei", "Japan", "South Korea", "North Korea", "Taiwan", "Hong Kong", "Macau", "Bangladesh", "Sri Lanka", "Nepal", "Bhutan", "Pakistan", "Afghanistan", "Iran", "Iraq", "Saudi Arabia", "UAE", "Oman", "Yemen", "Qatar", "Kuwait", "Bahrain", "Jordan", "Lebanon", "Syria", "Israel", "Palestine", "Turkey", "Cyprus", "Greece", "Italy", "Spain", "Portugal", "France", "Germany", "United Kingdom", "Ireland", "Netherlands", "Belgium", "Luxembourg", "Switzerland", "Austria", "Czech Republic", "Slovakia", "Hungary", "Poland", "Romania", "Bulgaria", "Serbia", "Croatia", "Bosnia and Herzegovina", "Montenegro", "North Macedonia", "Albania", "Kosovo", "Slovenia", "United States", "Canada", "Mexico", "Brazil", "Argentina", "Chile", "Peru", "Colombia", "Venezuela", "Ecuador", "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname", "French Guiana", "Australia", "New Zealand", "Papua New Guinea", "Fiji", "Solomon Islands", "Vanuatu", "New Caledonia", "Egypt", "Libya", "Tunisia", "Algeria", "Morocco", "Sudan", "South Sudan", "Ethiopia", "Eritrea", "Djibouti", "Somalia", "Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "Congo", "Democratic Republic of the Congo", "Angola", "Zambia", "Zimbabwe", "Mozambique", "Malawi", "South Africa", "Namibia", "Botswana", "Lesotho", "Eswatini"]

    occupations = ["Teacher", "Engineer", "Doctor", "Lawyer", "Accountant", "Nurse", "Salesperson", "Manager", "Chef", "Artist", "Software Developer", "Data Scientist", "Architect", "Pharmacist", "Dentist", "Veterinarian", "Police Officer", "Firefighter", "Paramedic", "Pilot", "Flight Attendant", "Electrician", "Plumber", "Carpenter", "Mechanic", "Hairdresser", "Beautician", "Photographer", "Journalist", "Writer", "Editor", "Translator", "Interpreter", "Psychologist", "Counselor", "Social Worker", "Financial Advisor", "Insurance Agent", "Real Estate Agent", "Marketing Specialist", "Public Relations Specialist", "Human Resources Manager", "Graphic Designer", "Web Designer", "UX Designer", "Product Manager", "Project Manager", "Business Analyst", "Systems Analyst", "Network Administrator", "Database Administrator", "Cybersecurity Specialist", "Librarian", "Museum Curator", "Zoologist", "Marine Biologist", "Environmental Scientist", "Geologist", "Meteorologist", "Astronomer", "Physicist", "Chemist", "Biologist", "Mathematician", "Statistician", "Economist", "Political Scientist", "Sociologist", "Anthropologist", "Archaeologist", "Historian", "Philosopher", "Theologian", "Actor", "Musician", "Dancer", "Choreographer", "Film Director", "Producer", "Screenwriter", "Fashion Designer", "Interior Designer", "Landscape Architect", "Urban Planner", "Civil Engineer", "Mechanical Engineer", "Electrical Engineer", "Chemical Engineer", "Aerospace Engineer", "Biomedical Engineer", "Environmental Engineer", "Nuclear Engineer", "Petroleum Engineer", "Agricultural Engineer", "Food Scientist", "Nutritionist", "Dietitian", "Personal Trainer", "Sports Coach", "Athlete", "Referee", "Umpire", "Tour Guide", "Travel Agent", "Hotel Manager", "Restaurant Manager", "Bartender", "Waiter/Waitress", "Housekeeping Staff", "Janitor", "Security Guard", "Locksmith", "Tailor", "Seamstress", "Jeweler", "Watchmaker", "Optician", "Optometrist", "Audiologist", "Speech Therapist", "Occupational Therapist", "Physical Therapist", "Massage Therapist", "Chiropractor", "Acupuncturist", "Naturopath", "Homeopath", "Midwife", "Doula", "Farmer", "Rancher", "Fisherman", "Forester", "Gardener", "Florist", "Botanist", "Zoologist", "Entomologist", "Paleontologist", "Geographer", "Cartographer", "Surveyor", "Air Traffic Controller", "Ship Captain", "Train Conductor", "Bus Driver", "Taxi Driver", "Truck Driver", "Courier", "Postal Worker", "Librarian", "Archivist", "Curator", "Conservator", "Restorer", "Printer", "Bookbinder", "Engraver", "Sculptor", "Painter", "Illustrator", "Animator", "Game Designer", "Voice Actor", "Stunt Performer", "Magician", "Circus Performer", "Street Performer", "Busker", "Tattoo Artist", "Piercer", "Makeup Artist", "Special Effects Artist", "Prosthetics Technician", "Orthodontist", "Endodontist", "Periodontist", "Oral Surgeon", "Radiologist", "Anesthesiologist", "Surgeon", "Cardiologist", "Neurologist", "Oncologist", "Pediatrician", "Geriatrician", "Psychiatrist", "Dermatologist", "Gynecologist", "Urologist", "Ophthalmologist", "Otolaryngologist", "Podiatrist", "Nephrologist", "Pulmonologist", "Rheumatologist", "Gastroenterologist", "Endocrinologist", "Hematologist", "Immunologist", "Pathologist", "Forensic Scientist", "Toxicologist", "Biochemist", "Microbiologist", "Virologist", "Geneticist", "Embryologist", "Ecologist", "Oceanographer", "Seismologist", "Volcanologist", "Hydrologist", "Glaciologist", "Climatologist", "Astronaut", "Cosmonaut", "Taikonaut"]

    languages = ["English", "Mandarin", "Malay", "Tamil", "Hokkien", "Cantonese", "Teochew", "Hakka", "Hainanese", "Hindi", "Bengali", "Urdu", "Punjabi", "Gujarati", "Malayalam", "Telugu", "Kannada", "Marathi", "Tagalog", "Indonesian", "Vietnamese", "Thai", "Burmese", "Khmer", "Lao", "Japanese", "Korean", "Arabic", "Persian", "Turkish", "Russian", "French", "German", "Spanish", "Portuguese", "Italian", "Greek", "Dutch", "Swedish", "Norwegian", "Danish", "Finnish", "Polish", "Czech", "Slovak", "Hungarian", "Romanian", "Bulgarian", "Serbian", "Croatian", "Bosnian", "Albanian", "Macedonian", "Slovenian", "Ukrainian", "Belarusian", "Lithuanian", "Latvian", "Estonian", "Georgian", "Armenian", "Azerbaijani", "Kazakh", "Uzbek", "Turkmen", "Kyrgyz", "Tajik", "Mongolian", "Tibetan", "Nepali", "Sinhala", "Dzongkha", "Tetum", "Fijian", "Samoan", "Tongan", "Maori", "Hawaiian", "Swahili", "Zulu", "Xhosa", "Afrikaans", "Amharic", "Somali", "Yoruba", "Igbo", "Hausa", "Wolof", "Fulani", "Oromo", "Hebrew", "Yiddish", "Latin", "Ancient Greek", "Sanskrit", "Classical Chinese", "Esperanto"]

    blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    ns_ranks = ["Private", "Lance Corporal", "Corporal", "Sergeant", "Staff Sergeant", "2nd Lieutenant", "Lieutenant", "Captain"]
    marital_statuses = ["Single", "Married", "Divorced", "Separated", "Widowed", "Civil Partnership", "Domestic Partnership", "Engaged", "Annulled"]
    religions = ["Buddhism", "Christianity", "Islam", "Hinduism", "Taoism", "No Religion"]
    dob = generate_date(datetime(1950, 1, 1), datetime(2024, 12, 31))

    towns = [
        "Ang Mo Kio", "Bedok", "Tampines", "Woodlands", "Jurong West", "Sengkang", "Punggol",
        "Yishun", "Hougang", "Jurong East", "Choa Chu Kang", "Bukit Batok", "Toa Payoh",
        "Serangoon", "Bukit Merah", "Pasir Ris", "Clementi", "Bishan", "Queenstown",
        "Bukit Panjang", "Kallang", "Geylang", "Marine Parade", "Novena", "Tanjong Pagar",
        "Bukit Timah", "Sembawang", "Central Area", "Rochor", "Orchard", "Newton",
        "Outram", "River Valley", "Downtown Core", "Marina South", "Straits View"
    ]

    streets = [
        "Orchard Road", "Serangoon Road", "Shenton Way", "Raffles Place", "Boon Lay Way",
        "Jurong Gateway Road", "Ang Mo Kio Avenue 3", "Tampines Avenue 5", "Woodlands Avenue 1",
        "Bedok North Street 1", "Punggol Central", "Sengkang East Way", "Yishun Ring Road",
        "Hougang Avenue 7", "Choa Chu Kang Avenue 4", "Bukit Batok East Avenue 3",
        "Toa Payoh Lorong 1", "Bishan Street 22", "Clementi Avenue 3", "Marine Parade Road",
        "Pasir Ris Drive 1", "Upper Serangoon Road", "Upper Thomson Road", "Bukit Timah Road",
        "Jalan Besar", "Victoria Street", "North Bridge Road", "South Bridge Road",
        "New Upper Changi Road", "Eu Tong Sen Street", "Telok Blangah Road", "Alexandra Road",
        "Joo Chiat Road", "Geylang Road", "Kallang Way", "Lavender Street", "Beach Road",
        "Balestier Road", "Bartley Road", "Braddell Road", "Bukit Panjang Ring Road",
        "Commonwealth Avenue", "Holland Road", "East Coast Road", "Sembawang Road",
        "Mandai Road", "Changi Road", "Upper East Coast Road", "Loyang Avenue",
        "Admiralty Drive", "Yio Chu Kang Road", "Lorong Chuan", "Kovan Road", "Simei Street 1"
    ]
    work_pass_types = ["Employment Pass", "S Pass", "Work Permit", "Dependent's Pass", "Long Term Visit Pass"]
    language_proficiencies = ["Basic", "Conversational", "Fluent", "Native"]

    races = ["Chinese", "Malay", "Indian", "Others"]
    religions = ["Buddhism", "Christianity", "Islam", "Hinduism", "Taoism", "No Religion"]
    towns = ["Ang Mo Kio", "Bedok", "Tampines", "Woodlands", "Jurong West", "Sengkang", "Punggol"]
    email_providers = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    sg_qualifications = ["PSLE", "N-Levels", "O-Levels", "A-Levels", "Diploma", "Bachelor's", "Master's", "PhD"]
    language_proficiencies = ["Basic", "Conversational", "Fluent", "Native"]
    ns_statuses = ["Pre-enlistee", "NSF", "NSman", "Exempted"]
    ns_ranks = ["Private", "Lance Corporal", "Corporal", "Sergeant", "Staff Sergeant", "2nd Lieutenant", "Lieutenant", "Captain"]
    work_pass_types = ["Employment Pass", "S Pass", "Work Permit", "Dependent's Pass", "Long Term Visit Pass"]

    citizenship = random.choice(["Singapore Citizen", "Singapore PR", "Foreigner"])
    name, name_generator = generate_name()
    profile = {
        "nric": generate_nric(),
        "name": name_generator(),
        "race": random.choice(races),
        "gender": random.choice(["Male", "Female"]),
        "date_of_birth": (datetime.now() - timedelta(days=random.randint(6570, 36500))).strftime("%Y-%m-%d"),
        "age": 0,
        "country_of_birth": random.choice(countries),
        "citizenship": citizenship,
        "religion": random.choice(religions),
        "marital_status": random.choice(marital_statuses),
        "address": {
            "block": f"{random.randint(1, 999)}",
            "street No.": f"{random.randint(1, 999)}",
            "street": f"{random.choice(streets)}",
            "unit": f"#{random.randint(1, 30)}-{random.randint(1, 999):03d}",
            "town": random.choice(towns),
            "postal_code": f"{random.randint(100000, 999999)}"
        },
        "phone_number": generate_phone_number(),
        "email": generate_random_email(),
        "occupation": random.choice(occupations),
        "cpf_number": generate_cpf_number(),
        "education": {
            "highest_qualification": random.choice(sg_qualifications),
            "institution": random.choice(["NUS", "NTU", "SMU", "SUTD", "Local Polytechnic", "Local JC", "Others"])
        },
        "languages": {
            "spoken": {lang: random.choice(language_proficiencies) for lang in random.sample(languages, random.randint(1, 3))},
            "written": {lang: random.choice(language_proficiencies) for lang in random.sample(languages, random.randint(1, 3))}
        },
        "height_cm": random.randint(150, 190),
        "weight_kg": random.randint(45, 100),
        "blood_type": random.choice(blood_types),
        "passport_number": generate_passport_number(),
        "drivers_license_number": generate_drivers_license(),
        "national_service": {
            "status": None,
            "rank": None
        },
        "immigration_status": None,
        "emergency_contact": {
            "name": name_generator(),
            "relationship": random.choice(["Parent", "Sibling", "Spouse", "Friend"]),
            "phone_number": generate_phone_number()
        },
        "deceased": random.choice([True, False])
    }

    profile["age"] = calculate_age(datetime.strptime(profile["date_of_birth"], "%Y-%m-%d"))

    if profile["gender"] == "Male" and profile["citizenship"] in ["Singapore Citizen", "Singapore PR"]:
        if profile["age"] < 18:
            profile["national_service"]["status"] = "Pre-enlistee"
        elif 18 <= profile["age"] <= 20:
            profile["national_service"]["status"] = "NSF"
            profile["national_service"]["rank"] = random.choice(ns_ranks[:5])
        elif profile["age"] > 20:
            profile["national_service"]["status"] = "NSman"
            profile["national_service"]["rank"] = random.choice(ns_ranks)

    if profile["citizenship"] == "Foreigner":
        profile["immigration_status"] = random.choice(work_pass_types)

    if profile["deceased"]:
        dob = datetime.strptime(profile["date_of_birth"], "%Y-%m-%d")
        age_in_days = profile["age"] * 365
        date_of_death = dob + timedelta(days=age_in_days)
        profile["date_of_death"] = date_of_death.strftime("%Y-%m-%d")

    return profile


def generate_profiles(n):
    return [generate_profile() for _ in range(n)]


