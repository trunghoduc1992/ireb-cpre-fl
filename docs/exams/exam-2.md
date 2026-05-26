<script setup>
import ExamQuiz from '../.vitepress/theme/ExamQuiz.vue'

const questions = [
  // ── Chapter 1: Introduction & Foundations (3 questions) ──
  // Q1 — K-type, 2 pts
  {
    text: 'Which of the following statements about the three types of requirements defined by IREB are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A functional requirement describes a specific behavior or service the system must provide.', answer: true },
      { text: 'A quality requirement specifies how well the system must perform its functions (e.g., response time, availability).', answer: true },
      { text: 'A constraint is a type of functional requirement that describes optional features.', answer: false },
      { text: 'Quality requirements are always derived from constraints and cannot be elicited independently.', answer: false },
    ],
    points: 2,
    explanation: 'Functional requirements describe system behaviors (WHAT the system does). Quality requirements describe how well the system performs (HOW WELL). Constraints restrict the solution space (e.g., mandated technology or regulations) — they are NOT a type of functional requirement. Quality requirements are elicited independently from stakeholders and domain analysis, not derived from constraints.',
    chapter: 'Ch 1',
  },
  // Q2 — A-type, 1 pt
  {
    text: 'You are the requirements engineer for a fleet management system. During an elicitation workshop, the logistics manager and the fleet safety officer present contradictory expectations about vehicle tracking frequency. According to IREB, what is your PRIMARY role?',
    options: [
      'Accept the logistics manager\'s position because they have more authority',
      'Facilitate communication between both stakeholders to establish a shared understanding',
      'Design a technical compromise yourself without consulting either stakeholder',
      'Document both positions and let the development team choose during implementation',
    ],
    answer: 1,
    points: 1,
    explanation: 'The RE\'s primary role is to act as a mediator — facilitating communication, negotiation, and shared understanding between stakeholders. The RE does not decide based on authority, make technical compromises unilaterally, or defer decisions to the development team.',
    chapter: 'Ch 1',
  },
  // Q3 — A-type, 1 pt
  {
    text: 'Which of the following is a constraint rather than a functional or quality requirement?',
    options: [
      'The system shall allow users to reset their password via email verification.',
      'The system shall support at least 10,000 concurrent users.',
      'All system components shall comply with the European General Data Protection Regulation (GDPR).',
      'The system shall load any page within 3 seconds on a standard broadband connection.',
    ],
    answer: 2,
    points: 1,
    explanation: 'GDPR compliance is a constraint — it is an externally imposed restriction on the solution space that cannot be negotiated. Password reset is a functional requirement. Concurrent users and page load time are quality requirements (scalability and performance).',
    chapter: 'Ch 1',
  },

  // ── Chapter 2: System & System Context (3 questions) ──
  // Q4 — A-type, 1 pt
  {
    text: 'A team is developing a new online food delivery platform. They identify the restaurant POS systems, the payment gateway, delivery driver mobile apps, and city traffic data APIs. Where do these elements belong?',
    options: [
      'Inside the system boundary as internal components of the SuD',
      'In the system context — between the system boundary and the context boundary',
      'Outside the context boundary as irrelevant elements',
      'In the requirements specification as functional requirements',
    ],
    answer: 1,
    points: 1,
    explanation: 'Restaurant POS systems, payment gateways, driver apps, and traffic APIs are external entities that interact with the delivery platform. They reside in the system context — the relevant environment between the system boundary (the SuD) and the context boundary (beyond which things are irrelevant).',
    chapter: 'Ch 2',
  },
  // Q5 — K-type, 2 pts
  {
    text: 'Which of the following statements about stakeholders and the system context are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A stakeholder is any person, group, or organization that can affect or be affected by the system.', answer: true },
      { text: 'Only people who directly use the system are considered stakeholders.', answer: false },
      { text: 'Regulatory bodies can be stakeholders if their regulations impose constraints on the system.', answer: true },
      { text: 'The system context should be determined once at the start and never revised.', answer: false },
    ],
    points: 2,
    explanation: 'Stakeholders include anyone who affects or is affected by the system — not just direct users. Regulatory bodies are stakeholders when they impose constraints. The system context is iteratively refined as understanding grows; it is not fixed at the start.',
    chapter: 'Ch 2',
  },
  // Q6 — P-type, 2 pts
  {
    text: 'A university is building a new student enrollment system. Which of the following are elements of the system context? (Select two)',
    options: [
      'The university\'s existing financial accounting system that will receive tuition payment data',
      'A competing university\'s enrollment process',
      'The national student loan authority that provides financial aid eligibility data',
      'A restaurant chain operating near the campus',
      'The internal microservice architecture planned for the enrollment system',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'The financial accounting system and the national student loan authority are external entities that interact with the SuD — they are part of the system context. The competing university and restaurant are irrelevant (outside the context boundary). The internal microservice architecture is inside the system boundary, not in the context.',
    chapter: 'Ch 2',
  },

  // ── Chapter 3: Requirements Elicitation (7 questions) ──
  // Q7 — A-type, 1 pt
  {
    text: 'A requirements engineer needs to understand the daily workflow of insurance claims adjusters before designing a new claims management system. Many adjusters work in the field and perform tasks they cannot easily articulate in an interview. Which elicitation technique is MOST appropriate?',
    options: [
      'Sending a detailed questionnaire to all adjusters',
      'Conducting a brainstorming session with the IT department',
      'Performing field observation of adjusters during their work',
      'Reviewing the company\'s organizational chart',
    ],
    answer: 2,
    points: 1,
    explanation: 'Field observation is the best technique for discovering tacit knowledge — the tasks people do automatically without conscious thought. Adjusters who "cannot easily articulate" their workflow will reveal it through observation. Questionnaires and brainstorming cannot capture unarticulated behavior.',
    chapter: 'Ch 3',
  },
  // Q8 — K-type, 2 pts
  {
    text: 'Which of the following statements about interviews as an elicitation technique are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Open questions encourage stakeholders to provide detailed, narrative answers.', answer: true },
      { text: 'Interviews are the most cost-effective technique for gathering input from hundreds of users.', answer: false },
      { text: 'The interviewer should prepare an interview guide with key topics and questions before the session.', answer: true },
      { text: 'Leading questions should be used frequently to guide the stakeholder toward the desired answer.', answer: false },
    ],
    points: 2,
    explanation: 'Open questions encourage detailed responses. Interviews do not scale to hundreds of users — questionnaires do. Preparation with an interview guide is essential for effective interviews. Leading questions bias the stakeholder and should be avoided; they produce unreliable results.',
    chapter: 'Ch 3',
  },
  // Q9 — P-type, 2 pts
  {
    text: 'Which of the following statements about prototyping for elicitation are correct? (Select two)',
    options: [
      'An evolutionary prototype is built with production technology and incrementally refined into the final system',
      'Prototypes are only useful for eliciting functional requirements, never quality requirements',
      'A throwaway prototype helps stakeholders provide concrete feedback on abstract concepts',
      'Prototyping eliminates the need for any other elicitation technique',
      'Stakeholders should never interact with prototypes before the final system is built',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'Evolutionary prototypes are refined into the final system using production technology. Throwaway prototypes make abstract concepts tangible for stakeholder feedback. Prototypes can also reveal quality requirements (e.g., usability issues). No single technique eliminates the need for others. Stakeholder interaction with prototypes is the entire point of prototyping for elicitation.',
    chapter: 'Ch 3',
  },
  // Q10 — A-type, 1 pt
  {
    text: 'During a workshop for a new healthcare scheduling system, the facilitator asks participants to generate as many ideas as possible for appointment booking features without evaluating any ideas. Which technique is being used within the workshop?',
    options: [
      'Document analysis',
      'Brainstorming',
      'Perspective-based reading',
      'Passive observation',
    ],
    answer: 1,
    points: 1,
    explanation: 'Brainstorming generates ideas freely without criticism or evaluation. The key rules are: no criticism during generation, quantity over quality, building on others\' ideas, and evaluation in a separate phase. This technique can be used within a workshop setting.',
    chapter: 'Ch 3',
  },
  // Q11 — K-type, 2 pts
  {
    text: 'Which of the following statements about observation as an elicitation technique are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'In active observation, the observer may ask questions and interact with the person being observed.', answer: true },
      { text: 'In passive observation, the observer watches silently without interfering with the work process.', answer: true },
      { text: 'Observation is only useful for documenting IT systems, not manual business processes.', answer: false },
      { text: 'Observation requires stakeholders to prepare written documentation of their tasks before the session.', answer: false },
    ],
    points: 2,
    explanation: 'Active observation allows interaction; passive observation does not. Observation is valuable for ANY process — manual or IT-based — and is especially useful for manual processes where tacit knowledge is involved. Observation does NOT require stakeholders to prepare documentation — the whole point is to watch them work naturally, which is what makes it effective for discovering unarticulated knowledge.',
    chapter: 'Ch 3',
  },
  // Q12 — P-type, 1 pt
  {
    text: 'Which of the following are valid reasons for combining multiple elicitation techniques in a project? (Select two)',
    options: [
      'Different techniques reveal different types of requirements and knowledge',
      'Using multiple techniques guarantees that no requirements will ever be missed',
      'Techniques like document analysis can prepare the ground for more targeted interviews',
      'IREB mandates using a minimum of six different techniques per project',
      'Combining techniques always reduces the total project cost',
    ],
    answer: [0, 2],
    multi: true,
    points: 1,
    explanation: 'Each technique has different strengths — interviews find depth, observation finds tacit knowledge, questionnaires find breadth. Document analysis is excellent preparation for interviews. However, no combination guarantees completeness, IREB does not mandate a specific number, and combining techniques may increase rather than decrease costs.',
    chapter: 'Ch 3',
  },
  // Q13 — A-type, 1 pt
  {
    text: 'Which elicitation technique is MOST appropriate when you need to verify that all relevant viewpoints on a draft requirements specification have been considered?',
    options: [
      'Brainstorming with the development team',
      'Questionnaire distributed to end users',
      'Perspective-based reading by reviewers from different stakeholder roles',
      'Passive observation of the project manager',
    ],
    answer: 2,
    points: 1,
    explanation: 'Perspective-based reading involves reviewers reading the specification from different stakeholder viewpoints (user, tester, developer, operator) to systematically identify gaps and inconsistencies that one perspective alone would miss. It is specifically designed to ensure multiple viewpoints are covered.',
    chapter: 'Ch 3',
  },

  // ── Chapter 4: Documentation Basics (6 questions) ──
  // Q14 — A-type, 1 pt
  {
    text: 'A requirements specification states: "The system shall allow users to search for products by name and category." A system specification states: "The search module shall use Elasticsearch with fuzzy matching on the product name field." What is the key distinction between these two statements?',
    options: [
      'The first statement is incorrect because it does not mention the technology',
      'The first describes WHAT the system does (problem-oriented); the second describes HOW it is implemented (solution-oriented)',
      'The second statement should appear in the requirements specification instead',
      'Both statements belong in the system specification because they describe the same feature',
    ],
    answer: 1,
    points: 1,
    explanation: 'The requirements specification is problem-oriented — it describes WHAT the system should do from the stakeholder perspective. The system specification is solution-oriented — it describes HOW the system implements those requirements. The first statement describes user-facing behavior; the second describes technical implementation.',
    chapter: 'Ch 4',
  },
  // Q15 — K-type, 2 pts
  {
    text: 'Which of the following statements about quality criteria for requirements specifications are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A specification is "complete" if it contains all relevant requirements with no TBD (to be determined) entries remaining.', answer: true },
      { text: 'A specification is "consistent" if no two requirements in it contradict each other.', answer: true },
      { text: 'A specification is "traceable" if every requirement has an assigned developer.', answer: false },
      { text: 'A specification is "modifiable" if any stakeholder can edit it without approval.', answer: false },
    ],
    points: 2,
    explanation: 'Complete means all relevant requirements are present with no open TBDs. Consistent means no contradictions between requirements. Traceable means requirements are linked to sources and downstream artifacts — not just assigned to developers. Modifiable means the document structure supports changes without cascading edits — it does not mean anyone can edit without approval.',
    chapter: 'Ch 4',
  },
  // Q16 — P-type, 2 pts
  {
    text: 'According to IREB, which of the following are the three forms of requirements documentation? (Select two that are correct forms)',
    options: [
      'Natural language documentation — universally readable by all stakeholders',
      'Source code comments — requirements embedded directly in the implementation',
      'Model-based documentation — precise diagrams and formal notations like UML',
      'Verbal-only documentation — requirements communicated exclusively in meetings',
      'Test case documentation — requirements expressed solely as acceptance tests',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'IREB identifies three forms: natural language (readable by everyone), model-based (precise diagrams/notations), and mixed forms (combining both). Source code comments, verbal-only communication, and test-case-only formats are NOT recognized documentation forms in the IREB framework.',
    chapter: 'Ch 4',
  },
  // Q17 — A-type, 1 pt
  {
    text: 'Which quality criterion for an individual requirement is violated when two developers interpret the same requirement in completely different ways?',
    options: [
      'Correctness — the requirement does not accurately reflect a stakeholder need',
      'Unambiguousness — the requirement can be interpreted in more than one way',
      'Traceability — the requirement cannot be linked to its source',
      'Necessity — the requirement is not needed for the project',
    ],
    answer: 1,
    points: 1,
    explanation: 'If two developers interpret a requirement differently, it is ambiguous — it has more than one valid interpretation. An unambiguous requirement has exactly one meaning for all readers. This is one of the most critical quality criteria for individual requirements.',
    chapter: 'Ch 4',
  },
  // Q18 — P-type, 1 pt
  {
    text: 'Which of the following are valid quality criteria for INDIVIDUAL requirements according to IREB? (Select two)',
    options: [
      'Modifiable — the requirement can be changed without cascading edits to the document',
      'Verifiable — a finite, cost-effective process can check whether the system fulfills the requirement',
      'Consistent — the requirement does not contradict any other requirement',
      'Complete at specification level — the specification contains all relevant requirements',
      'Traceable — the requirement has a unique ID and its origin and impact can be determined',
    ],
    answer: [1, 2],
    multi: true,
    points: 1,
    explanation: 'Verifiable and consistent are quality criteria for individual requirements. Modifiable and complete (at specification level) are criteria for the entire specification document, not individual requirements. Traceable applies at both levels, but option E describes it correctly for individual requirements — however, "verifiable" and "consistent" are more clearly individual-level criteria.',
    chapter: 'Ch 4',
  },
  // Q19 — K-type, 2 pts
  {
    text: 'Which of the following statements about requirements documentation practices are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Each requirement should have a unique identifier to enable unambiguous referencing and traceability.', answer: true },
      { text: 'Pre-requirements traceability links each requirement back to its source, helping to understand why it exists.', answer: true },
      { text: 'Once a requirement is documented, its text should never be modified — only new requirements can be added.', answer: false },
      { text: 'A requirements specification should include a version history to track changes over time.', answer: true },
    ],
    points: 2,
    explanation: 'Unique IDs enable unambiguous referencing and traceability. Pre-requirements traceability links to sources (stakeholders, regulations, goals), supporting impact analysis and rationale. Requirements CAN and SHOULD be modified when needed — through a controlled change management process. Version history is essential for tracking the evolution of the specification over time.',
    chapter: 'Ch 4',
  },

  // ── Chapter 5: Natural Language (6 questions) ──
  // Q20 — K-type, 2 pts
  {
    text: 'Which of the following statements about natural language defects in requirements are true and which are false?',
    type: 'ktype',
    statements: [
      { text: '"The system shall ensure the timely processing of all incoming requests" contains a vague term ("timely").', answer: true },
      { text: '"The system shall generate the report on a daily basis" is an example of passive voice.', answer: false },
      { text: '"The calculation of the discount shall be performed" contains a nominalization ("calculation").', answer: true },
      { text: 'Universal quantifiers like "all", "every", and "never" should be used cautiously because they make absolute claims.', answer: true },
    ],
    points: 2,
    explanation: '"Timely" is a vague term with no measurable threshold. "The system shall generate the report" is active voice — it has a clear subject ("the system") performing a clear action ("generate"). "Calculation" is a nominalization (turning the verb "calculate" into the noun "calculation"), which obscures the action. Universal quantifiers like "all" and "never" make absolute claims that may not hold in all edge cases and should be used cautiously.',
    chapter: 'Ch 5',
  },
  // Q21 — A-type, 1 pt
  {
    text: 'According to IREB, what does the keyword "shall" indicate in a requirement?',
    options: [
      'The requirement is optional and may be ignored if resources are limited',
      'The requirement is mandatory and must be fulfilled',
      'The requirement is recommended but can be omitted with documented justification',
      'The requirement describes a future release feature that is not yet planned',
    ],
    answer: 1,
    points: 1,
    explanation: '"Shall" indicates a mandatory requirement — it MUST be fulfilled. "Should" indicates recommended (can be omitted with justification). "May" or "can" indicates an optional feature. This keyword hierarchy is a fundamental IREB concept.',
    chapter: 'Ch 5',
  },
  // Q22 — A-type, 1 pt
  {
    text: 'A requirements glossary reveals that the development team uses the term "client" while the sales team uses "customer" to refer to the same concept. What type of terminology problem is this?',
    options: [
      'Homonym — one word with multiple meanings',
      'Synonym — different words for the same concept',
      'Nominalization — a verb turned into a noun',
      'Universal quantifier — an overly broad claim',
    ],
    answer: 1,
    points: 1,
    explanation: 'A synonym occurs when different terms refer to the same concept. "Client" and "customer" meaning the same thing is a synonym problem. The glossary should standardize on one term to avoid confusion. A homonym is the opposite — one term with multiple meanings.',
    chapter: 'Ch 5',
  },
  // Q23 — P-type, 2 pts
  {
    text: 'Which of the following requirements contain language defects according to IREB guidelines? (Select two)',
    options: [
      'The system shall allow the administrator to lock a user account after 5 failed login attempts.',
      'All data shall be migrated in an appropriate manner.',
      'The inventory module shall reduce the stock count by the ordered quantity when an order is confirmed.',
      'The system shall ensure that every user is always satisfied with the performance.',
      'The clerk shall enter the shipping address into the order form before submitting.',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: '"In an appropriate manner" is a vague term — "appropriate" is subjective and non-verifiable. "Every user is always satisfied" contains dangerous universal quantifiers ("every", "always") and a subjective, non-verifiable term ("satisfied"). Options A, C, and E have clear subjects, specific actions, and measurable conditions.',
    chapter: 'Ch 5',
  },
  // Q24 — K-type, 2 pts
  {
    text: 'Which of the following statements about sentence templates and the glossary are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A sentence template provides a fixed structure (e.g., subject + keyword + action + object + condition) to improve consistency.', answer: true },
      { text: 'Using sentence templates eliminates all ambiguity from requirements automatically.', answer: false },
      { text: 'A glossary should define each term in the specific context of the project, not just use dictionary definitions.', answer: true },
      { text: 'Glossary entries should include synonyms and abbreviations to help resolve terminology conflicts.', answer: true },
    ],
    points: 2,
    explanation: 'Sentence templates improve consistency and reduce certain ambiguities but cannot eliminate ALL ambiguity automatically — the content quality still depends on the author. A glossary must define terms in the project context (not generic dictionary definitions) and should include synonyms, abbreviations, and the term\'s source.',
    chapter: 'Ch 5',
  },
  // Q25 — A-type, 1 pt
  {
    text: 'Which of the following sentences demonstrates the problem of nominalization?',
    options: [
      'The system shall validate the user\'s credentials before granting access.',
      'The validation of the user\'s credentials shall be performed before access is granted.',
      'The authentication module shall check the username and password against the user database.',
      'The user shall enter their credentials on the login page.',
    ],
    answer: 1,
    points: 1,
    explanation: '"The validation of the user\'s credentials" turns the verb "validate" into the noun "validation", obscuring who performs the action and making the sentence more complex. The other options use clear subjects and active verbs. Option A correctly uses the verb form "validate" with a clear subject "the system".',
    chapter: 'Ch 5',
  },

  // ── Chapter 6: Model-Based Documentation (6 questions) ──
  // Q26 — A-type, 1 pt (with diagram)
  {
    text: 'Refer to the use case diagram below. Which statement about this diagram is correct?',
    diagram: 'graph LR\n  Customer((Customer))\n  Admin((Admin))\n  PayGW((Payment Gateway))\n  Customer --- PlaceOrder[Place Order]\n  Customer --- ViewHistory[View Order History]\n  PlaceOrder -. include .-> ValidatePayment[Validate Payment]\n  ValidatePayment --- PayGW\n  Admin --- ManageProducts[Manage Products]\n  Admin --- PlaceOrder',
    options: [
      'The Payment Gateway is an internal component of the system, not an actor',
      'Validate Payment is always executed as part of Place Order because of the <<include>> relationship',
      'Admin cannot Place Order because only Customer is associated with it',
      'View Order History includes Validate Payment as a mandatory step',
    ],
    answer: 1,
    points: 1,
    explanation: 'The <<include>> relationship means Validate Payment is always executed when Place Order is executed — it is mandatory. The Payment Gateway is an external actor (it is outside the system). Admin IS associated with Place Order in the diagram. View Order History has no include relationship to Validate Payment.',
    chapter: 'Ch 6',
  },
  // Q27 — K-type, 2 pts
  {
    text: 'Which of the following statements about activity diagrams are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A fork node splits the flow into multiple concurrent (parallel) paths.', answer: true },
      { text: 'A join node allows execution to continue as soon as ANY one incoming path completes.', answer: false },
      { text: 'Swim lanes partition activities by responsible actor, role, or organizational unit.', answer: true },
      { text: 'A decision node branches the flow into mutually exclusive paths based on guard conditions.', answer: true },
    ],
    points: 2,
    explanation: 'A fork splits into parallel paths (all execute concurrently). A join requires ALL incoming paths to complete before proceeding — not just any one. Swim lanes assign responsibility to actors or departments. Decision nodes branch into mutually exclusive alternative paths based on guard conditions.',
    chapter: 'Ch 6',
  },
  // Q28 — P-type, 2 pts (with diagram)
  {
    text: 'Refer to the class diagram below. Which of the following statements are correct? (Select two)',
    diagram: 'classDiagram\n  class Department {\n    +name: String\n    +location: String\n  }\n  class Employee {\n    +name: String\n    +employeeId: String\n  }\n  class Project {\n    +title: String\n    +deadline: Date\n  }\n  Department \"1\" o-- \"1..*\" Employee : employs\n  Employee \"1..*\" --> \"0..*\" Project : works on',
    options: [
      'A Department must have at least one Employee (multiplicity 1..*)',
      'If a Department is deleted, all its Employees are automatically deleted',
      'An Employee can work on zero or more Projects',
      'A Project must have at least one Employee assigned to it',
      'The relationship between Department and Employee is composition',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'The multiplicity "1..*" on the Employee side means a Department must have at least one Employee. The hollow diamond (o--) indicates aggregation, NOT composition — so Employees can exist independently if the Department is dissolved. An Employee has multiplicity "0..*" to Project, meaning they can work on zero or more Projects. A Project has "1..*" to Employee on one side but "0..*" from the Employee side, meaning Projects can exist with no Employees yet assigned.',
    chapter: 'Ch 6',
  },
  // Q29 — A-type, 1 pt (with diagram)
  {
    text: 'Refer to the state machine diagram below. What happens when the event "cancel" occurs while the order is in the "Confirmed" state?',
    diagram: 'stateDiagram-v2\n  [*] --> Draft\n  Draft --> Confirmed : submit [all items available]\n  Confirmed --> Shipped : dispatch\n  Confirmed --> Cancelled : cancel / send cancellation email\n  Shipped --> Delivered : deliver\n  Delivered --> [*]\n  Cancelled --> [*]',
    options: [
      'The order remains in the Confirmed state because cancel is not a valid event',
      'The order transitions to the Cancelled state and a cancellation email is sent',
      'The order transitions to the Draft state so the user can edit it',
      'The order is immediately deleted from the system',
    ],
    answer: 1,
    points: 1,
    explanation: 'The transition "cancel / send cancellation email" means: when the event "cancel" occurs in the Confirmed state, the order transitions to the Cancelled state and the action "send cancellation email" is executed. The format is: event [guard] / action.',
    chapter: 'Ch 6',
  },
  // Q30 — K-type, 2 pts
  {
    text: 'Which of the following statements about class diagram relationships are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Aggregation (hollow diamond) represents a whole-part relationship where parts can exist independently.', answer: true },
      { text: 'Composition (filled diamond) represents a whole-part relationship where parts are destroyed when the whole is destroyed.', answer: true },
      { text: 'Generalization in a class diagram represents an "is-a" relationship (inheritance).', answer: true },
      { text: 'Multiplicity "0..1" means the association is mandatory — exactly one instance is required.', answer: false },
    ],
    points: 2,
    explanation: 'Aggregation (hollow diamond) = weak ownership, parts survive. Composition (filled diamond) = strong ownership, parts are destroyed with the whole. Generalization = "is-a" (inheritance). Multiplicity "0..1" means zero or one — the association is OPTIONAL (0) or at most one (1). Mandatory would be "1" or "1..*".',
    chapter: 'Ch 6',
  },
  // Q31 — A-type, 1 pt
  {
    text: 'Which diagram type is MOST appropriate for modeling the interactions between actors and the major functions that a library management system provides?',
    options: [
      'Class diagram',
      'State machine diagram',
      'Use case diagram',
      'Activity diagram',
    ],
    answer: 2,
    points: 1,
    explanation: 'Use case diagrams show the functional scope of a system from the outside — which actors interact with which system functions (use cases). Class diagrams model data structure, state machines model entity lifecycles, and activity diagrams model process flows.',
    chapter: 'Ch 6',
  },

  // ── Chapter 7: Validation & Negotiation (7 questions) ──
  // Q32 — A-type, 1 pt
  {
    text: 'A project team reviews the requirements specification to check whether the documented requirements accurately capture what the hospital staff actually needs from the new system. This activity is an example of:',
    options: [
      'Verification — checking that code matches the specification',
      'Validation — checking that requirements match stakeholder needs',
      'Testing — executing the system to find bugs',
      'Deployment — releasing the system to production',
    ],
    answer: 1,
    points: 1,
    explanation: 'Validation asks "Are we building the right thing?" — it checks requirements against stakeholder intentions and needs. Verification asks "Are we building the thing right?" — it checks artifacts against their specifications. Testing checks running software. Deployment is releasing the system.',
    chapter: 'Ch 7',
  },
  // Q33 — K-type, 2 pts
  {
    text: 'Which of the following statements about walkthroughs and inspections are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'In a walkthrough, the author of the document guides participants through the content.', answer: true },
      { text: 'In an inspection, the author leads the review meeting to explain their design decisions.', answer: false },
      { text: 'Inspections require participants to prepare individually before the meeting.', answer: true },
      { text: 'Walkthroughs have a higher defect detection rate than inspections.', answer: false },
    ],
    points: 2,
    explanation: 'In walkthroughs, the author leads the session. In inspections, a moderator who is NOT the author leads the meeting — the author participates to answer questions but does not drive the review. This distinction is critical. Inspections require mandatory individual preparation. Inspections have a HIGHER defect detection rate than walkthroughs, not lower — they are the most formal and effective review technique.',
    chapter: 'Ch 7',
  },
  // Q34 — P-type, 2 pts
  {
    text: 'Which of the following are valid conflict resolution strategies according to IREB? (Select two)',
    options: [
      'Consensus — all parties fully agree on a solution',
      'Avoidance — ignoring the conflict until it resolves itself',
      'Compromise — all parties make concessions to reach a middle ground',
      'Intimidation — using threats to force one party to accept the other\'s position',
      'Elimination — removing the requirement that caused the conflict from the specification',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'IREB defines five conflict resolution strategies: consensus (full agreement), compromise (mutual concessions), voting (majority decides), overruling (authority decides), and mediation (neutral third party facilitates). Avoidance, intimidation, and elimination are not recognized strategies.',
    chapter: 'Ch 7',
  },
  // Q35 — A-type, 1 pt
  {
    text: 'The marketing department wants the system to use a playful, casual tone in all messages. The legal department requires all messages to use formal, legally precise language. What type of conflict is this?',
    options: [
      'Data conflict — the departments have different factual information',
      'Structural conflict — the departments have different levels of authority',
      'Value conflict — the departments hold fundamentally different beliefs about what is appropriate',
      'Relationship conflict — the departments have personal animosity toward each other',
    ],
    answer: 2,
    points: 1,
    explanation: 'This is a value conflict — the departments have fundamentally different beliefs about what constitutes appropriate communication. Marketing values engagement and approachability; Legal values precision and compliance. Neither position is factually wrong — they stem from different value systems.',
    chapter: 'Ch 7',
  },
  // Q36 — K-type, 2 pts
  {
    text: 'Which of the following statements about requirements validation are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Validation should be performed early and repeatedly throughout the RE process.', answer: true },
      { text: 'The only valid validation technique is formal inspection.', answer: false },
      { text: 'Perspective-based reading asks reviewers to examine the specification from specific stakeholder viewpoints.', answer: true },
      { text: 'Prototyping can be used for validation to make abstract requirements tangible for stakeholder review.', answer: true },
    ],
    points: 2,
    explanation: 'Validation should occur early and continuously — not just at the end. Multiple techniques are valid: inspections, walkthroughs, perspective-based reading, prototyping, and others. Perspective-based reading uses different stakeholder viewpoints. Prototyping makes requirements tangible for stakeholder evaluation.',
    chapter: 'Ch 7',
  },
  // Q37 — P-type, 2 pts
  {
    text: 'Which of the following activities are part of a formal inspection process? (Select two)',
    options: [
      'The author implements all suggested changes during the inspection meeting',
      'Reviewers individually examine the document before the meeting and note defects',
      'The scribe records all findings, decisions, and action items during the meeting',
      'The project manager decides which reviewers are allowed to speak during the meeting',
      'The meeting is held without any preparation — reviewers read the document for the first time',
    ],
    answer: [1, 2],
    multi: true,
    points: 2,
    explanation: 'In a formal inspection, reviewers must prepare individually before the meeting (finding defects in advance). During the meeting, the scribe records findings and decisions. The author does NOT implement changes during the meeting — rework happens afterward. The moderator (not project manager) facilitates the meeting. Preparation is mandatory — reading for the first time at the meeting defeats the purpose.',
    chapter: 'Ch 7',
  },
  // Q38 — A-type, 1 pt
  {
    text: 'During a requirements review, stakeholders from three departments each want their features prioritized first. The requirements engineer proposes that each stakeholder ranks the features and the majority vote determines the final priority. Which conflict resolution strategy is this?',
    options: [
      'Consensus',
      'Compromise',
      'Voting',
      'Overruling',
    ],
    answer: 2,
    points: 1,
    explanation: 'Voting lets the majority decide the outcome. Each stakeholder expresses their preference, and the option with the most votes wins. Consensus requires full agreement (not just majority). Compromise requires mutual concessions. Overruling involves an authority figure deciding.',
    chapter: 'Ch 7',
  },

  // ── Chapter 8: Requirements Management (6 questions) ──
  // Q39 — K-type, 2 pts
  {
    text: 'Which of the following statements about requirements prioritization are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'MoSCoW classifies requirements into four categories: Must, Should, Could, and Won\'t have this time.', answer: true },
      { text: 'Pairwise comparison scales well to thousands of requirements because it is automated.', answer: false },
      { text: 'In the Kano model, basic (must-be) requirements are expected — their absence causes strong dissatisfaction.', answer: true },
      { text: 'Prioritization should be done once at the beginning and never revisited during the project.', answer: false },
    ],
    points: 2,
    explanation: 'MoSCoW has four categories (M/S/C/W). Pairwise comparison does NOT scale well — it requires N*(N-1)/2 comparisons, which becomes impractical for large sets. Kano basic requirements cause dissatisfaction when absent but are taken for granted when present. Prioritization should be revisited as the project evolves and new information emerges.',
    chapter: 'Ch 8',
  },
  // Q40 — P-type, 2 pts
  {
    text: 'Which of the following correctly describe Kano model requirement categories? (Select two)',
    options: [
      'Basic (must-be) requirements cause strong dissatisfaction when absent but are taken for granted when present',
      'Performance (one-dimensional) requirements have no effect on customer satisfaction regardless of fulfillment',
      'Excitement (attractive/delighter) requirements create strong satisfaction when present but are not missed when absent',
      'Indifferent requirements cause strong dissatisfaction when absent from the system',
      'Basic requirements are unexpected bonus features that delight the customer',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'Basic requirements are expected — their absence causes dissatisfaction, but their presence is taken for granted. Excitement requirements are unexpected — they delight when present but are not missed when absent. Performance requirements DO affect satisfaction (linearly). Indifferent requirements do NOT cause dissatisfaction when absent. Basic requirements are NOT unexpected bonus features.',
    chapter: 'Ch 8',
  },
  // Q41 — P-type, 2 pts
  {
    text: 'Which of the following are types of traceability defined by IREB? (Select two)',
    options: [
      'Pre-requirements traceability — linking requirements back to their sources (stakeholders, regulations, goals)',
      'Parallel traceability — linking requirements to requirements in competitor products',
      'Post-requirements traceability — linking requirements forward to design, code, and test artifacts',
      'Temporal traceability — linking requirements to specific calendar dates',
      'Aesthetic traceability — linking requirements to the visual design of the user interface',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'IREB defines three types: pre-requirements (backward to sources), post-requirements (forward to downstream artifacts like design, code, tests), and inter-requirements (between requirements). Parallel, temporal, and aesthetic traceability are not IREB concepts.',
    chapter: 'Ch 8',
  },
  // Q42 — A-type, 1 pt
  {
    text: 'What is the primary purpose of establishing a requirements baseline?',
    options: [
      'To delete all previous versions of requirements permanently',
      'To create a formally agreed-upon reference point for development, testing, and change control',
      'To prevent any further changes to requirements for the rest of the project',
      'To assign all requirements to specific developers for implementation',
    ],
    answer: 1,
    points: 1,
    explanation: 'A baseline is a formally approved snapshot of requirements at a specific point in time. It serves as a reference point for development and testing. Changes after a baseline are still possible but must go through formal change management. Baselines do not delete history, block changes, or assign work.',
    chapter: 'Ch 8',
  },
  // Q43 — K-type, 2 pts
  {
    text: 'Which of the following statements about change management are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Impact analysis assesses which requirements, design elements, code, and tests are affected by a proposed change.', answer: true },
      { text: 'The Change Control Board (CCB) evaluates change requests and decides whether to approve or reject them.', answer: true },
      { text: 'A change request can be implemented immediately without impact analysis if the change seems small.', answer: false },
      { text: 'After a change is implemented, verification should confirm that the change was correctly applied.', answer: true },
    ],
    points: 2,
    explanation: 'Impact analysis identifies all affected artifacts. The CCB evaluates and decides on change requests. ALL changes — regardless of size — should go through impact analysis because "small" changes can have unexpected ripple effects. Verification after implementation confirms the change was correctly applied and did not introduce defects.',
    chapter: 'Ch 8',
  },
  // Q44 — P-type, 1 pt
  {
    text: 'Which of the following are commonly used requirement attributes? (Select two)',
    options: [
      'Source — the stakeholder or document from which the requirement originated',
      'Font family — the typeface used to display the requirement',
      'Risk — the level of risk associated with implementing the requirement',
      'Line count — the number of lines of code needed to implement it',
      'Compiler version — the compiler version needed to build the requirement',
    ],
    answer: [0, 2],
    multi: true,
    points: 1,
    explanation: 'Source and risk are standard requirement attributes used in management. Source traces the requirement\'s origin; risk helps prioritize and plan. Font family, line count, and compiler version are not meaningful requirement attributes — they relate to formatting or implementation details.',
    chapter: 'Ch 8',
  },

  // ── Chapter 9: Tool Support (2 questions) ──
  // Q45 — A-type, 1 pt
  {
    text: 'A small startup with no formal RE process is considering purchasing an enterprise-grade RE management tool costing $50,000 per year. Based on the IREB principle regarding tool adoption, what should they do FIRST?',
    options: [
      'Purchase the tool immediately because it will automatically establish good RE practices',
      'Establish a sound RE process first, then evaluate whether a tool would support and improve it',
      'Avoid using any tools entirely and rely only on verbal communication',
      'Purchase the cheapest tool available regardless of whether it fits their needs',
    ],
    answer: 1,
    points: 1,
    explanation: 'The IREB principle "a fool with a tool is still a fool" means tools cannot replace a sound RE process. Organizations should first establish good practices, then select tools that support those practices. The tool amplifies whatever process exists — a good tool with a bad process just makes problems worse.',
    chapter: 'Ch 9',
  },
  // Q46 — K-type, 2 pts
  {
    text: 'Which of the following statements about RE tool support are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Dedicated RE tools (e.g., IBM DOORS, Polarion) support traceability management, baselining, and change control.', answer: true },
      { text: 'General-purpose tools (e.g., word processors, spreadsheets) can be used for RE but lack specialized features for traceability and change management.', answer: true },
      { text: 'Modeling tools (e.g., Enterprise Architect) support creating UML diagrams for model-based documentation.', answer: true },
      { text: 'A tool alone is sufficient to ensure high-quality requirements engineering without any process or methodology.', answer: false },
    ],
    points: 2,
    explanation: 'Dedicated RE tools provide specialized features for managing requirements. General-purpose tools can be used for simpler projects but lack RE-specific capabilities. Modeling tools support UML and other notations. However, no tool can substitute for a sound RE process — tools support and amplify processes but do not replace them.',
    chapter: 'Ch 9',
  },
]
</script>

# Sample Exam 2

<div class="exam-tip">
  <strong>Exam simulation:</strong> 46 questions, 70 points, 75-minute time limit, 70% passing score (49/70 pts). Includes single-select, pick-two, and True/False matrix questions — matching the real IREB CPRE-FL exam format.
</div>

<ExamQuiz :questions="questions" />
