
<html>
<head>
    <link rel="stylesheet" href="style.css">
    <title>CS 499 - Computer Science Capstone</title>
</head>
<body>

<div class="overlay"></div>

<div class="content">
    <h1>CS 499 - Computer Science Capstone</h1>

<p>Hi! My name is Shakira Baker, and I have attended Southern New Hampshire University for about two years. Before enrolling at SNHU, I had already successfully completed computer science related coursework at previous colleges and through my career in the Army National Guard. This ePortfolio highlights the skills I have developed throughout my computer science journey at SNHU. Below, you will find a link to a code review where I thoroughly explain the starting code and the enhancements I planned to make. You will also find a description of my capstone project which includes an explanation of how I satisfied the three required categories which are Software Design/Engineering, Algorithms and Data Structures, and Databases. Lastly, I have included a Professional Self-Assessment to further describe the valuable tools and knowledge I have gained during my time at SNHU, which have better prepared me to pursue various careers within the computer science field.</p>

<details open>
    <summary>Code Review</summary>
    <p>This is my code review providing a more in depth explanation of the project I chose to enhance and the changes I plan to make to improve the project.</p>
    <p>
        <a href="https://drive.google.com/file/d/1TppenujYq8zQyBxP8UxVRcQMRahrPOal/view?usp=drive_link" target="_blank">Watch Code Review Part 1</a>
    </p>
    <p>
        <a href="https://drive.google.com/file/d/1hBxWl3TuKWJgc8fN1FtX9Rb2k8O1Kxcm/view?usp=drive_link" target="_blank">Watch Code Review Part 2</a>
    </p>
</details>     

<details open>
        <summary>Project Details</summary>
        <p>The artifact I chose to enhance is one of the first projects I completed when I started my journey at SNHU back in January or February of 2023. It is a text-based video game that I developed using Python in IT 140: Introduction to Scripting. The goal of the project was to develop a text-based video game that allowed a user to enter the text “Go North, Go South, Go East, or Go West” to navigate through a maze of rooms that was provided to us. We were able to decide the theme of the game, what each room would be, and what items would be available to collect in each room. Each room only had certain directions available depending on the direction of the openings displayed in the provided map. The player had to visit each room and collect an item to have everything necessary to kill the boss in the final room. If the player failed to collect all the items they would lose the boss fight, otherwise they would succeed. I chose this artifact because it was a simple project with a lot of potential, and I knew that with more development knowledge and skills, I could take it much further. Even in its original form, the project demonstrated my ability to code in Python, write modular functions for specific tasks, and create well-organized, well-commented code that was easy to follow. I enjoyed building it and wanted to improve the user experience by making it more engaging.</p><br>

<div class="centered-text">
        <p>🛠️<b>Software Design/Engineering</b></p>
        <img src="login_screen.png" alt="Software Design Diagram" class="center-image">
        
<p> To satisfy this category I enhanced the project significantly by converting it from Python to C#, restructuring it into multiple classes and methods. I added a database to support user login, saving, and loading game states, which didn't exist before. I’ve also started building the interface using WinForms, separating the login and game screens into two forms for better organization. Security features like input validation, password masking, and character limits were added to the login screen, along with password hashing for secure storage and verification. I implemented error handling to avoid null values and improve performance, and used internal classes with private variables accessed through getters and setters to strengthen encapsulation. These improvements highlight my growth in software development, from basic scripting to building more complex, secure, and user-friendly applications.</p>
<a href="https://drive.google.com/file/d/1TppenujYq8zQyBxP8UxVRcQMRahrPOal/view?usp=drive_link" target="_blank">View full software design/engineering narrative</a>
<br><br>
        
<p>📚 <b>Algorithms and Data Structures</b></p>
<p>To satisfy the Algorithms and Data Structures category, I expanded the project’s complexity by adding a graphical user interface using WinForms and integrating a database to allow players to save and load their game states. I also implemented a secure hashing algorithm to protect player passwords, improved the MovePlayer method for more efficient handling of UI button clicks, and optimized the WinForms interface by reusing controls to improve performance. Creating the WinForms interface showcases my ability to design a functional UI that dynamically hides or displays controls as needed. Integrating the database demonstrates my skills in building an SQLite database connected to the UI and developing methods to manipulate data directly through the interface. Additionally, my object-oriented programming skills are reflected in how I restructured the entire project into multiple classes, applied encapsulation, and transitioned from standalone functions to methods within internal classes, each serving a specific role in the overall functionality of the game.</p>
<a href="https://drive.google.com/file/d/1TppenujYq8zQyBxP8UxVRcQMRahrPOal/view?usp=drive_link" target="_blank">View full algorithms and data structures narrative</a>
<br><br>

<p>🗄️ <b>Databases</b></p>
<p>To satisfy the Database category, I created a database using SQLite and integrated it into the project to allow players to create accounts and save their game progress. Players can now start a new game or continue from a saved state, a feature that did not exist in the original project. I developed methods to provide full CRUD functionality and connected these methods to buttons in the WinForms UI, allowing database actions to be performed directly through user interactions. The database includes two well-structured tables, one for user login details and another for tracking player progress. I designed both tables to enforce data integrity by preventing null values in critical fields and ensuring that primary key columns are unique. These design choices showcase my ability to implement effective schema design and input validation. I also demonstrated secure coding practices by using parameterized queries to protect against SQL injection attacks. Additionally, I ensured that the database tables are only created if they do not already exist and implemented logic to update an existing save rather than creating duplicate entries, maintaining data consistency by leveraging the unique username constraint. Through these enhancements, I’ve demonstrated my ability to design, implement, and securely integrate a functional database within a desktop application.</p>
<a href="https://drive.google.com/file/d/1TppenujYq8zQyBxP8UxVRcQMRahrPOal/view?usp=drive_link" target="_blank">View full databases narrative</a><br><br>

<p>✅ <b>Course Outcomes Satisfied</b></p>
</div>

</details>

<details open>
        <summary>Professional Self Assessment</summary>
        <p>This is my self assessment</p>
</details>
</div>

</body>
</html>

