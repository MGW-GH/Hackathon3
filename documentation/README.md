![Logo/header img](/documentation/readme-images/quizards-text-logo.webp) ![Quizard img](/documentation/readme-images/quizzard-img.webp)

# Project overview 

Quizards is a digital platform for Trivia enthusiasts. Built with Django, it allows registered users to tackle 5 quiz questions daily. With a user-friendly interface and engaging content, it aims to make learning convenient and interactive. 

This daily quiz format aims to set the app apart by fostering consistent engagement while enhancing general knowledge retention.

### How To Play

Sign up/sign in as a user, quizzes will then be available for completion. Quizzes will be presented in multiple choice formats of 5 questions, feedback on scores will be presented on completion.

# List of features

![features image template]()

#### Feature 1 etc
#### Feature 2 etc

# UX/UI

### Audience Properties:
- Key Demographics: Ages 18-35, students, young professionals.  
- Key Psychographics: Enjoys learning and self-improvement, digital-savvy.  
- Pain Points: Difficulty finding time for learning, desire for regular progress tracking.  
- Buying Process: Looks for reviews, tests free trials, appreciates straightforward subscriptions.  
- Brands & Tone: Inspired by brands like Duolingo, Khan Academy; appreciates an engaging yet informational tone.

### Job
The main job of this website is to encourage user registration and daily engagement. It should clearly present the app's benefits, showcase its daily quiz format, and motivate users to sign up and participate regularly.

### Messaging and tone

Brand Archetype: Sage (knowledge).  
Tone Characteristics:  
- Informative, Engaging: Make trivia fun and accessible.  
- Trustworthy, Conversational: Build confidence with straightforward dialogue.  
- Respectful, Caring: Show understanding of user goals and learning journeys.  
- Matter-of-fact, Upbeat: Communicate with enthusiasm.

Example Messaging:  
“Sharpen your mind, day by day.”  
“Daily quizzes, boundless knowledge.”  
“Engage, learn, excel.”

### Design direction
- Simple, intuitive design: Reflects ease of use.  
- Engaging graphics: Visualize the daily learning journey.  
- Clear navigation: Highlights daily quiz feature.  
- Bright color scheme: Inspires excitement and curiosity.

### Website Structure
- Home Section: Welcome message, quick overview, and CTA to register/login.  
- Daily Quiz Details: Explain daily  and benefits.  
- How It Works: Step-by-step guide to engaging with content.  
- User Testimonials: Reviews from enthusiastic learners.  
- Benefits: Clear bullet points on learning and engagement advantages.  
- Call to Action: Encouragement to sign up and start playing.  
- Footer: Contact details, community forums, and support links.

### Wireframes

![ui image 1](/documentation/readme-images/wireframes-img.png)

- Initial designs produced using https://app.scene.io/ 
- Design rolled back to a simple three page design during the iterative process.

### Colour scheme

Initial colour schemes were produced using http://colormind.io/ colour palette was chosen to be cohesive, while being bright and engaging.

![Colour scheme image](/documentation/readme-images/color-scheme-img.png)

Variables were used within the CSS file to call colours as they were needed:

- Royal Blue: #4A5DE8;
- Burnt Ocre: #FF9F1C;
- Off-white: #F5F5F5;
- Pastel yellow: #FFEA00;
- Charcol: #333333;

Initial colour schemes were produced using http://colormind.io/ colour palette was chosen to be cohesive, while being bright and engaging.

Adjustments from initial designs were made where there was any accessability issue relating to choices.

### Typography & Iconography

In developing our full-stack Django site, we chose to utilize Bootstrap's default fonts to keep the project scope manageable. By leveraging these pre-designed fonts, we were able to maintain a consistent and professional aesthetic without the added complexity of custom typography.

This decision not only streamlined the design process but also allowed us to focus on core functionalities and features, ensuring we could deliver a high-quality user experience efficiently. Using Bootstrap's default fonts provided a solid foundation for our site's visual identity while simplifying development and enhancing overall productivity.

### Database Schema

![ERD Diamgram](/documentation/readme-images/erd-img.png)

Database Schema Entity Relationship Diagram (ERD) for Quizards displaying relationships between feature components saved within the database

Lucidchart was used to create the ERD for Quizards. To satisfy the application needs, models were created for the project. These include:

- **User** (User is created on signup, linked to results)
- **Questions** (Questions model exits in database to store and return questions)
- **Results** (Linked to User)

# Testing

Website tested for responsivity of all pages and components by sight and manual testing, for three screen sizes Mobile, Laptop, and Desktop.

## HTML Validation
HTML run through W3 validator.

![HTML img 1]()
![HTML error img 1]()

Current build works with no errors in browser and mobile views.
Bugs prioritsed to next iteration due to hard stop deadline.

## CSS Validation
All CSS run through Jigsaw validator no issues.

![css valid img1]() ![css valid img2]()

## Lighthouse

![lighthouse scores performance](/documentation/readme-images/quizzards_lighthouse.png)

All pages run through Lighthouse to check scores. 

![lighthouse scores img1](/documentation/readme-images/lighthouse-2-img.png) ![lighthouse scores img2](/documentation/readme-images/lighthouse-3-img.png)

Acceptable scores in all categories. No major issues.

## Deployment

https://quiz-heads-c1d86a4688ff.herokuapp.com

## Citation of ALL sources(code, images, text, tutorials and UX/UI tools)

- Initial wireframes https://scene.io
- Colour scheme http://colormind.io/
- Question generation https://perplexity.ai
- Wizard icons created by Freepik - Flaticon https://www.flaticon.com/free-icons/wizard
- Quiz Wizard image https://pro-quiz-wizard.netlify.app/
- Quizards text logo https://www.textstudio.com/
- Stackoverflow https://stackoverflow.co/
  
## Future features

Future planned features added to backlog for next iteration include:

- Categories of questions
- Ability for users to add questions to the site once approved
- Ensure questions already answered wont be repeated for the same user
- Users can answer 5 daily questions and this cannot be repeated
