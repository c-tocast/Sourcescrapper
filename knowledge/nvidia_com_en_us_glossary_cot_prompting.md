# Fuente original: https://nvidia.com/en-us/glossary/cot-prompting/

What is Chain of Thought (CoT) Prompting?
| NVIDIA Glossary
This site requires Javascript in order to view all its content. Please enable Javascript in order to access all the functionality of this web site. Here are the
instructions how to enable JavaScript in your web browser.
What Is Chain of Thought Prompting?
Chain of Thought (CoT) is a prompt engineering technique that helps
large language models
(LLMs) reason with more accuracy, the same way you would get a human to: by asking it to show its work. CoT prompting works by first asking a question and providing an answer as input. When a second question is asked, the LLM uses the pattern established from the first question and answer to generate an answer for the second question.
Related
How Scaling Laws Enable AI Reasoning
Chain of Thought: An Approach for Reasoning
CoT is used in a new group of AI reasoning models called long-thinking or test-time scaling models. Other models need the user to prompt the model to break down problems into a series of steps. Test-time scaling systematically automates CoT reasoning. The model is self-directed, so it can initiate and manage its own thoughts without relying on a user's prompt sequence. The automation in the Chain of Thought process is a breakthrough in AI's ability to handle complex reasoning tasks. It aims to improve the language model's performance on complex tasks, such as math, logic, planning, and decision making. These advancements will build more intelligent
agentic AI
systems, driving far-reaching outcomes for use cases across healthcare, robotics, and finance, where complex decision making is a must.
Generative AI, Scaling Laws, and Chain of Thought Prompting
It should be noted that CoT prompting isn't inherently a generative AI technique; rather, it’s a prompt engineering method used within
generative AI
systems, particularly large language models, and is applied to a scaling law called test-time compute or “long thinking.” This scaling law suggests that the longer a model "thinks" or processes information internally before producing an output, the better its answer becomes.
Specifically:
The scaling law for CoT relates to post-training performance improvements.
It demonstrates that allowing an AI model to go through more internal reasoning steps (producing hidden thinking tokens) before giving a final, correct answer leads to better performance.
This scaling law appears to have no upper limit, similar to training scaling laws, but it's exponential. This means that to continue improving outputs, the AI needs to "think" for increasingly longer periods.
Recent research has shown that observational scaling laws can reliably predict the gains from post-training techniques like Chain of Thought. This indicates that CoT is not just a technique but follows a predictable scaling pattern across different model sizes and capabilities.
Why Is Chain of Thought Prompting Important?
CoT prompting is important because it significantly enhances the reasoning capabilities of LLMs, leading to more accurate and reliable outputs for complex tasks. This technique breaks down intricate problems into manageable steps, mirroring human-like reasoning processes.
Key Benefits
Improved Problem Solving: CoT enables LLMs to decompose complex problems into a series of intermediate steps, allowing for more accurate reasoning and better handling of multifaceted tasks.
Enhanced Transparency: By providing a glimpse into the model's thought process, CoT allows users to better understand and debug the reasoning paths when they go wrong.
Versatility: CoT has been successfully applied to a wide range of tasks requiring reasoning, making it a versatile technique for various applications.
Cost: It can be implemented easily without the need for fine-tuning, making it a cost-effective method to improve model performance.
Reduced Errors: By guiding models through a structured thought process, CoT helps in reducing logical errors and enhancing the overall accuracy of responses.
CoT Prompting Is Particularly Valuable in Areas Such As:
Mathematics and arithmetic problems
Common-sense and symbolic reasoning tasks
Complex decision-making scenarios, including fields like robotics
By leveraging the extensive knowledge LLMs are trained on and enhancing their logical reasoning capabilities, Chain of Thought prompting has become a crucial technique in pushing the boundaries of AI's problem-solving abilities.
How Does CoT Prompting Work?
Initial Prompting:
The process starts with an initial question (Q1) and its corresponding answer (A1), which serves as an example for the LLM. This establishes a structured reasoning pattern.
Pattern Recognition:
The LLM analyzes the structure and logic used in the initial question and answer. By understanding this pattern, the model prepares to apply similar reasoning to future questions.
Sequential Questioning:
When a subsequent question (Q2) is presented, the LLM leverages the reasoning demonstrated in the Q1-A1 pair to generate an informed response to Q2. This chaining allows for a more coherent and logical flow of information, as each question-answer pair builds upon the previous one.
Reducing Human Involvement:
In CoT prompting, the human role in directly crafting prompts is minimized. Instead of manually designing each prompt, humans focus on providing quality feedback during the training phase. This feedback is incorporated through
Reinforcement Learning
with Human Feedback (RLHF), where humans evaluate the model’s responses and offer corrective guidance. The LLM uses this feedback to refine its understanding and boosts the accuracy of its generated answers.
How Does Chain of Thought Prompting Improve LLM Model Performance?
CoT prompting significantly improves LLM model performance by enhancing the model’s reasoning capabilities and problem-solving skills. This technique guides LLMs through a structured thought process, leading to more precise and reliable outputs, especially for complex tasks.
Enhanced Reasoning and Problem Solving
CoT prompting enables LLMs to break down intricate problems into manageable steps, mirroring human-like reasoning processes. This approach is particularly effective for tasks that require multi-step problem solving, such as mathematical word problems, symbolic reasoning, and common-sense reasoning tasks. By encouraging the model to articulate intermediate reasoning steps, CoT prompting helps identify and correct errors along the way, resulting in more accurate final answers.
Enhanced Contextual Understanding
CoT prompting helps LLMs maintain context throughout complex reasoning tasks. By structuring the thought process, it ensures that the model considers all relevant information, leading to more contextually appropriate and accurate responses. This is particularly beneficial for tasks requiring deep analysis or the application of multiple concepts.
Error Reduction
The step-by-step nature of CoT prompting allows LLMs to identify and correct errors during the reasoning process. This self-correction mechanism significantly reduces the likelihood of incorrect final outputs, especially in tasks involving multiple calculations or logical steps.
In conclusion, Chain of Thought prompting substantially improves LLM accuracy by enhancing reasoning capabilities, providing structured problem-solving approaches, and enabling better error detection and correction. This technique has proven particularly effective for complex tasks requiring multi-step reasoning, demonstrating significant improvements across various benchmarks and problem domains.
Getting Started With Chain of Thought Prompting.
To learn more, read our explainer on
Scaling Laws
.
Related
How Scaling Laws Enable AI Reasoning
Next Steps
What Is Agentic AI?
Agentic AI uses sophisticated reasoning and iterative planning to autonomously solve complex, multi-step problems.
Learn More
Natural Language Processing Explained
Natural language processing is a technology that leverages computers and software to derive meaning from human language—written or spoken.
Learn More
Large Language Models Explained
Large language models (LLMs) are deep learning algorithms that can recognize, summarize, translate, predict, and generate content using very large datasets.
Learn More
Company Information
About Us
Investors
Venture Capital (NVentures)
NVIDIA Foundation
Research
Corporate Sustainability
Technologies
Careers
News and Events
Newsroom
Company Blog
Technical Blog
Webinars
Stay Informed
Events Calendar
GTC AI Conference
NVIDIA On-Demand
Popular Links
Developers
Partners
Executive Insights
Startups and VCs
NVIDIA Connect for ISVs
Documentation
Technical Training
Professional Services for Data Science
Follow NVIDIA
NVIDIA
United States
Privacy Policy
Your Privacy Choices
Terms of Service
Accessibility
Corporate Policies
Product Security
Contact
Copyright © 2026 NVIDIA Corporation