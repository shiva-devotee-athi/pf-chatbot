import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import simple
my_pf_details = """"Where did you complete your school education, and how has it shaped your interest in IT?

I completed my school education at XYZ High School. It was there that I first developed an interest in IT through a computer science class that introduced me to coding and problem-solving techniques.

Which university or college did you attend for your undergraduate studies, and what was your major?

I attended ABC University for my undergraduate studies, where I majored in Computer Science. The comprehensive curriculum and hands-on projects helped me build a strong foundation in various aspects of IT.

Can you describe any significant projects or research you worked on during your undergraduate studies?

One significant project I worked on was developing a mobile application for campus navigation. This project involved extensive research, coding, and collaboration with a team, and it significantly improved my skills in mobile development and teamwork.

Did you pursue any postgraduate education? If so, what specialization did you choose and why?

Yes, I pursued a Master's degree in Data Science. I chose this specialization because of my keen interest in data analysis and machine learning, which I believe are crucial areas in the IT industry today.

What programming languages or technical skills did you learn during your education that you find most useful in the IT industry?

During my education, I learned several programming languages such as Java, Python, and SQL. I found Python particularly useful for data analysis and machine learning projects, while SQL has been invaluable for database management.

Did you participate in any internships or co-op programs during your studies? If so, what did you learn from those experiences?

I completed an internship at a tech startup where I worked on developing web applications. This experience taught me practical skills in front-end and back-end development, as well as how to work in a fast-paced, dynamic environment.

Were you involved in any extracurricular activities or clubs related to IT or technology during your academic years?

Yes, I was an active member of the Computer Science Club, where we organized coding competitions and tech talks. I also participated in hackathons, which provided me with opportunities to apply my skills in real-world scenarios and collaborate with peers.

How do you stay updated with the latest trends and advancements in the IT field after completing your formal education?

I stay updated by following tech blogs, subscribing to industry newsletters, and participating in online courses and webinars. Additionally, I am an active member of professional IT forums and communities where I can learn from and network with other professionals.

Have you obtained any certifications relevant to the IT industry? How have they contributed to your professional growth?

I have obtained certifications such as Certified Scrum Master and AWS Certified Solutions Architect. These certifications have enhanced my knowledge and skills in agile methodologies and cloud computing, respectively, making me more versatile and effective in my roles.

Can you provide an example of a challenging academic project you completed and how you overcame any obstacles during that time?

One challenging project was developing an AI-based chatbot for customer service. The main obstacle was integrating natural language processing capabilities. I overcame this by conducting thorough research, seeking guidance from professors, and collaborating with classmates to find innovative solutions."""


s_t = nltk.tokenize.sent_tokenize(language="english", text=my_pf_details)
w_t = nltk.tokenize.word_tokenize(
    language="english", preserve_line=True, text=my_pf_details)
t_w_t = nltk.tokenize.TreebankWordDetokenizer()
print(s_t, len(s_t))
# print(w_t)
# print(t_w_t.tokenize(my_pf_details))
