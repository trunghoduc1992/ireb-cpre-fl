<script setup>
import ExamQuiz from '../.vitepress/theme/ExamQuiz.vue'

const questions = [
  // ── Chapter 1: Introduction & Foundations (3 questions) ──
  // Q1 — A-type, 1pt
  {
    text: 'You are a new requirements engineer joining a large automotive project. During the kick-off meeting, the project manager asks you to explain the three types of requirements according to IREB. Which answer correctly lists all three types?',
    options: [
      'User stories, epics, and acceptance criteria',
      'Functional requirements, quality requirements, and constraints',
      'Business requirements, stakeholder requirements, and solution requirements',
      'Mandatory requirements, optional requirements, and deferred requirements',
    ],
    answer: 1,
    points: 1,
    explanation: 'IREB classifies requirements into three types: functional requirements (what the system does), quality requirements (how well it does it, e.g., performance, usability, security), and constraints (restrictions on the solution space, e.g., technology mandates, regulatory rules). This classification is fundamental to the CPRE-FL syllabus.',
    chapter: 'Ch 1',
  },
  // Q2 — K-type, 2pts
  {
    text: 'Which of the following statements about requirements engineering are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Requirements engineering consists of four core activities: elicitation, documentation, validation & negotiation, and management.', answer: true },
      { text: 'The four core RE activities must always be performed in strict sequential order.', answer: false },
      { text: 'The requirements engineer acts as a mediator between stakeholders and the development team.', answer: true },
      { text: 'Requirements engineering is only necessary in waterfall projects, not in agile ones.', answer: false },
    ],
    points: 2,
    explanation: 'RE has four core activities (elicitation, documentation, validation & negotiation, management) that are performed iteratively and concurrently — not sequentially. The RE acts as a mediator, facilitating communication and building shared understanding. RE is needed regardless of the process model (waterfall, agile, or hybrid).',
    chapter: 'Ch 1',
  },
  // Q3 — P-type, 2pts
  {
    text: 'A company is developing a new e-commerce platform. Which TWO of the following are quality requirements? (Select two)',
    options: [
      'The system shall allow customers to add items to a shopping cart.',
      'The search results page shall load within 2 seconds under a load of 10,000 concurrent users.',
      'The system shall be developed using the company\'s existing Oracle database infrastructure.',
      'The system shall be available 99.95% of the time, measured monthly.',
      'The system shall calculate shipping costs based on destination and package weight.',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Loading within 2 seconds (performance) and 99.95% availability (reliability) are quality requirements — they describe HOW WELL the system performs. Adding items to a cart and calculating shipping costs are functional requirements (WHAT the system does). Using Oracle is a constraint (a restriction on the solution space).',
    chapter: 'Ch 1',
  },

  // ── Chapter 2: System & System Context (3 questions) ──
  // Q4 — A-type, 1pt
  {
    text: 'A logistics company is building a fleet management system. During context analysis, the RE identifies GPS satellites, a fuel card provider API, government road traffic regulations, and an internal HR system. Which of these is MOST likely outside the context boundary (i.e., part of the irrelevant environment)?',
    options: [
      'GPS satellites that provide vehicle location data',
      'The fuel card provider API that transmits fuel consumption data',
      'Government road traffic regulations affecting route planning',
      'The internal HR system that manages employee vacation schedules',
    ],
    answer: 3,
    points: 1,
    explanation: 'The HR vacation system is least relevant to fleet management — it does not directly interact with or influence the SuD. GPS, fuel card API, and traffic regulations all directly affect fleet management functionality. However, context boundaries are project-specific, and the HR system might become relevant if the fleet system needs to know driver availability.',
    chapter: 'Ch 2',
  },
  // Q5 — K-type, 2pts
  {
    text: 'Which of the following statements about the system context are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'The system boundary separates the System under Development (SuD) from its context.', answer: true },
      { text: 'The context boundary separates the relevant environment from the irrelevant environment.', answer: true },
      { text: 'Setting the context boundary too narrowly risks overlooking important stakeholders or interfaces.', answer: true },
      { text: 'Once the context boundary is defined, it must never be changed during the project.', answer: false },
    ],
    points: 2,
    explanation: 'The system boundary separates the SuD from its context, while the context boundary separates relevant from irrelevant environment. A too-narrow context boundary risks missing important influences. Context boundaries should be reviewed and adjusted as understanding grows — they are not fixed permanently.',
    chapter: 'Ch 2',
  },
  // Q6 — P-type, 1pt
  {
    text: 'A bank is developing a new online banking portal. Which TWO of the following are stakeholders of the system? (Select two)',
    options: [
      'The bank\'s compliance department, which must ensure regulatory adherence',
      'A competing bank that offers a similar product',
      'The end customers who will use the portal to manage their accounts',
      'A software company that built an unrelated internal tool five years ago',
      'The central bank that sets interest rates for the national economy',
    ],
    answer: [0, 2],
    multi: true,
    points: 1,
    explanation: 'Stakeholders are persons or organizations that have a direct or indirect influence on the requirements of the system or are affected by it. The compliance department influences requirements through regulations, and end customers use the system directly. A competing bank, an unrelated software vendor, and the central bank (unless specific regulations apply) are not stakeholders of this particular project.',
    chapter: 'Ch 2',
  },

  // ── Chapter 3: Requirements Elicitation (7 questions) ──
  // Q7 — A-type, 1pt
  {
    text: 'You are the RE for a hospital information system. Nurses claim they follow the documented medication dispensing procedure, but medication errors persist. Which elicitation technique would BEST reveal the actual process being followed?',
    options: [
      'Sending a questionnaire about the medication procedure to all nurses',
      'Conducting interviews with the head nurse about the documented procedure',
      'Performing field observation of nurses during actual medication rounds',
      'Organizing a brainstorming session with the IT department',
    ],
    answer: 2,
    points: 1,
    explanation: 'Field observation (especially passive observation) reveals what people actually do rather than what they say or believe they do. Observation captures tacit knowledge, workarounds, and deviations from documented processes that interviews and questionnaires cannot uncover.',
    chapter: 'Ch 3',
  },
  // Q8 — A-type, 1pt
  {
    text: 'Which of the following is NOT a characteristic of a well-facilitated requirements workshop?',
    options: [
      'It brings together stakeholders with different perspectives',
      'A neutral facilitator guides the discussion and manages conflicts',
      'The facilitator makes all final decisions about conflicting requirements',
      'Results are documented during or immediately after the workshop',
    ],
    answer: 2,
    points: 1,
    explanation: 'The facilitator guides the process but does NOT make decisions about requirements. The facilitator ensures productive discussion, manages conflicts, and keeps the group on track. Decision-making authority rests with the stakeholders, not the facilitator.',
    chapter: 'Ch 3',
  },
  // Q9 — K-type, 2pts
  {
    text: 'Which of the following statements about elicitation techniques are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Interviews are well-suited for exploring individual perspectives in depth but are time-consuming for large groups.', answer: true },
      { text: 'Questionnaires allow follow-up questions and interactive clarification with respondents.', answer: false },
      { text: 'A throwaway prototype is built to explore ideas and is then discarded, not evolved into the final system.', answer: true },
      { text: 'Brainstorming requires that every idea be critically evaluated immediately when proposed.', answer: false },
    ],
    points: 2,
    explanation: 'Interviews provide depth but do not scale well. Questionnaires are one-directional — no interactive follow-up is possible. Throwaway prototypes are deliberately discarded after learning from them (unlike evolutionary prototypes). Brainstorming explicitly forbids criticism during the idea-generation phase to encourage creative thinking.',
    chapter: 'Ch 3',
  },
  // Q10 — K-type, 2pts
  {
    text: 'Which of the following statements about observation as an elicitation technique are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'In active observation, the observer may ask questions and interact with the person being observed.', answer: true },
      { text: 'In passive observation, the observer watches silently without interfering with the observed process.', answer: true },
      { text: 'Observation can reveal tacit knowledge and workarounds that stakeholders may not mention in interviews.', answer: true },
      { text: 'Observation is the most cost-effective technique and should always be used instead of interviews.', answer: false },
    ],
    points: 2,
    explanation: 'Active observation allows interaction; passive observation does not. Observation uniquely captures tacit knowledge, real workflows, and undocumented workarounds. However, observation is time-consuming and impractical for all situations — it complements rather than replaces other techniques.',
    chapter: 'Ch 3',
  },
  // Q11 — A-type, 1pt
  {
    text: 'A company is replacing its legacy accounting system. Thousands of pages of existing documentation, forms, and regulations exist. Which elicitation technique should be applied FIRST?',
    options: [
      'Brainstorming with the development team',
      'Document analysis (system archaeology)',
      'Prototyping the new system\'s user interface',
      'Conducting a stakeholder workshop',
    ],
    answer: 1,
    points: 1,
    explanation: 'Document analysis (also called system archaeology) is the ideal starting point when extensive existing documentation exists. It reveals current business rules, data structures, and regulatory constraints without requiring stakeholder time. Findings then inform subsequent interviews and workshops.',
    chapter: 'Ch 3',
  },
  // Q12 — P-type, 2pts
  {
    text: 'You need to gather requirements from 500 geographically distributed sales representatives for a new CRM system. Which TWO techniques are MOST appropriate for this situation? (Select two)',
    options: [
      'Individual interviews with each of the 500 representatives',
      'A questionnaire (survey) distributed electronically to all representatives',
      'A single workshop with all 500 representatives in one room',
      'Observation of a representative sample of sales representatives in the field',
      'Having all 500 representatives write free-form requirement documents',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Questionnaires scale efficiently to large, distributed groups and can gather quantitative data. Observing a representative sample captures real work practices and tacit knowledge. Interviewing all 500 is impractical. A workshop with 500 people is unmanageable. Free-form documents from 500 people would yield inconsistent, unstructured input.',
    chapter: 'Ch 3',
  },
  // Q13 — P-type, 2pts
  {
    text: 'Which TWO of the following are advantages of prototyping as an elicitation technique? (Select two)',
    options: [
      'Prototypes help stakeholders visualize the system and provide concrete feedback',
      'Prototypes eliminate the need for any written requirements documentation',
      'Prototypes help discover requirements that stakeholders cannot articulate in abstract terms',
      'Prototypes are always cheaper than writing natural language requirements',
      'Prototypes guarantee that no requirements will be missed',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'Prototypes make abstract concepts tangible, helping stakeholders visualize the system and provide concrete feedback. They are especially valuable for discovering requirements that stakeholders struggle to articulate abstractly (the "I will know it when I see it" effect). Prototypes do not replace documentation, are not always cheaper, and cannot guarantee completeness.',
    chapter: 'Ch 3',
  },

  // ── Chapter 4: Documentation Basics (6 questions) ──
  // Q14 — A-type, 1pt
  {
    text: 'An RE is writing a specification for a medical device. One requirement states: "The system shall display the patient heart rate." A reviewer notes that this requirement is incomplete. Which quality criterion for individual requirements is violated?',
    options: [
      'Consistency — it contradicts other requirements',
      'Completeness — it omits display format, update frequency, range, and error handling',
      'Traceability — it cannot be linked to a source',
      'Correctness — heart rate is not a valid medical parameter',
    ],
    answer: 1,
    points: 1,
    explanation: 'The requirement is incomplete — it does not specify the display format (numeric, graph?), update frequency, valid range, what happens when the sensor fails, units of measurement, or acceptable accuracy. A complete requirement would address all these aspects.',
    chapter: 'Ch 4',
  },
  // Q15 — A-type, 1pt
  {
    text: 'Which of the following is NOT a quality criterion for an individual requirement according to IREB?',
    options: [
      'Unambiguous — it can be interpreted in only one way',
      'Verifiable — a test or review can determine whether it is met',
      'Modifiable — it can be changed without cascading edits to the document',
      'Traceable — its origin and downstream artifacts can be identified',
    ],
    answer: 2,
    points: 1,
    explanation: 'Modifiability is a quality criterion for the entire specification, not for individual requirements. Individual requirement quality criteria include: unambiguous, complete, correct, verifiable, consistent, necessary, traceable, and feasible. Modifiability applies to how the document as a whole is structured.',
    chapter: 'Ch 4',
  },
  // Q16 — K-type, 2pts
  {
    text: 'Which of the following statements about requirements documentation are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A requirements specification describes WHAT the system shall do from the stakeholder perspective.', answer: true },
      { text: 'A system specification describes HOW the system will realize the requirements from the developer perspective.', answer: true },
      { text: 'IEEE 830 (now ISO/IEC/IEEE 29148) provides a reference structure for software requirements specifications.', answer: true },
      { text: 'Every requirement in a specification must have a unique identifier to enable traceability and referencing.', answer: true },
    ],
    points: 2,
    explanation: 'A requirements specification is problem-oriented (WHAT), while a system specification is solution-oriented (HOW). IEEE 830/29148 is the classic SRS reference structure. Unique identifiers are essential for traceability, cross-referencing, and change management. All four statements are correct according to the IREB syllabus.',
    chapter: 'Ch 4',
  },
  // Q17 — K-type, 2pts
  {
    text: 'Which of the following statements about documentation quality criteria are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Consistency at the specification level means no two requirements contradict each other.', answer: true },
      { text: 'Completeness at the specification level means all relevant requirements and their interactions are documented.', answer: true },
      { text: 'A requirement is verifiable if a tester can design a test to determine whether it has been met.', answer: true },
      { text: 'A requirement is correct if it is written in grammatically proper English.', answer: false },
    ],
    points: 2,
    explanation: 'Consistency means no contradictions. Specification-level completeness means all relevant requirements are present. Verifiability means a test can confirm fulfillment. Correctness means the requirement accurately reflects a stakeholder need — it has nothing to do with grammar.',
    chapter: 'Ch 4',
  },
  // Q18 — P-type, 2pts
  {
    text: 'Which TWO of the following are valid reasons for using natural language combined with models (mixed documentation forms)? (Select two)',
    options: [
      'Natural language provides context and rationale that models cannot easily express',
      'Mixed forms eliminate the need for a glossary',
      'Models reduce ambiguity for structural and behavioral aspects compared to pure text',
      'Mixed forms guarantee that all stakeholders can read the documentation without training',
      'Using both forms allows the RE to skip the validation step',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'Natural language excels at context, rationale, and background information, while models reduce ambiguity for structure and behavior. Mixed forms leverage the strengths of both. They do not eliminate the glossary need, do not guarantee readability without training (models require training), and never skip validation.',
    chapter: 'Ch 4',
  },
  // Q19 — P-type, 1pt
  {
    text: 'Which TWO of the following are quality criteria that apply to the entire specification (not individual requirements)? (Select two)',
    options: [
      'Unambiguous — each requirement has only one interpretation',
      'Modifiable — the document structure allows changes without cascading edits',
      'Complete — all relevant requirements and their interactions are documented',
      'Verifiable — each requirement can be tested',
      'Correct — each requirement reflects an actual stakeholder need',
    ],
    answer: [1, 2],
    multi: true,
    points: 1,
    explanation: 'Modifiability and completeness (at the specification level) are quality criteria for the entire document. Unambiguous, verifiable, and correct are criteria for individual requirements. Note that completeness also applies at the individual requirement level (all necessary detail is present), but specification-level completeness means all requirements are present.',
    chapter: 'Ch 4',
  },

  // ── Chapter 5: Natural Language (6 questions) ──
  // Q20 — A-type, 1pt
  {
    text: 'A requirement reads: "All reports shall always be generated correctly for every user in all situations." Which natural language defect is present?',
    options: [
      'Nominalization',
      'Passive voice without agent',
      'Universal quantifiers (all, every, always) making the requirement untestable',
      'Use of an incorrect obligation keyword',
    ],
    answer: 2,
    points: 1,
    explanation: 'The words "all," "always," "every," and "all situations" are universal quantifiers that make the requirement practically untestable. How would you verify that something works correctly in literally ALL situations? Requirements should specify concrete, bounded conditions rather than universal claims.',
    chapter: 'Ch 5',
  },
  // Q21 — A-type, 1pt
  {
    text: 'Which of the following requirements correctly uses the IREB obligation keywords?',
    options: [
      '"The system could encrypt passwords at rest if time permits."',
      '"It would be nice if the system validated email addresses."',
      '"The system shall authenticate users before granting access to patient records."',
      '"Password encryption needs to happen eventually."',
    ],
    answer: 2,
    points: 1,
    explanation: '"Shall" is the correct mandatory obligation keyword per IREB (and RFC 2119). "Could," "would be nice," and "needs to" are informal expressions that do not communicate a clear obligation level. The three levels are: "shall" (mandatory), "should" (recommended), and "may" (optional).',
    chapter: 'Ch 5',
  },
  // Q22 — A-type, 1pt
  {
    text: 'A glossary entry for "Customer" in a project reads: "A person or organization that has purchased at least one product from the online shop." Which problem does this glossary entry help prevent?',
    options: [
      'Universal quantifiers in requirements',
      'Homonyms — where "customer" might mean different things to different stakeholders (e.g., registered visitor vs. paying buyer)',
      'Passive voice in requirements',
      'Missing obligation keywords',
    ],
    answer: 1,
    points: 1,
    explanation: 'A glossary definition prevents homonym problems by establishing one agreed-upon meaning. Without it, marketing might interpret "customer" as any visitor, while accounting might interpret it as someone who has paid. The glossary creates shared understanding across all stakeholders.',
    chapter: 'Ch 5',
  },
  // Q23 — K-type, 2pts
  {
    text: 'Which of the following statements about natural language in requirements are true and which are false?',
    type: 'ktype',
    statements: [
      { text: '"The calculation of the discount is performed by the system" contains a nominalization ("calculation").', answer: true },
      { text: '"Invoices shall be sent to customers" uses passive voice that obscures the responsible actor.', answer: true },
      { text: 'The keyword "shall" indicates a mandatory requirement that must be fulfilled.', answer: true },
      { text: 'The keyword "may" indicates a mandatory requirement that must be fulfilled.', answer: false },
    ],
    points: 2,
    explanation: '"Calculation" is a nominalization (verb "calculate" turned into a noun). "Invoices shall be sent" is passive voice — it does not specify WHO sends them. "Shall" means mandatory. "May" means optional, not mandatory.',
    chapter: 'Ch 5',
  },
  // Q24 — K-type, 2pts
  {
    text: 'Which of the following statements about sentence templates and glossaries are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Sentence templates provide a consistent structure (subject, obligation keyword, action, object, condition) that reduces ambiguity.', answer: true },
      { text: 'A glossary should document synonyms and abbreviations in addition to term definitions.', answer: true },
      { text: 'Sentence templates automatically eliminate all types of ambiguity from requirements.', answer: false },
      { text: 'Highlighting glossary terms in requirements text signals that the term has a specific project-defined meaning.', answer: true },
    ],
    points: 2,
    explanation: 'Sentence templates enforce structure and reduce ambiguity but cannot eliminate ALL types. Glossaries should include synonyms, abbreviations, and context-specific definitions. Highlighting glossary terms signals a defined meaning that readers should reference.',
    chapter: 'Ch 5',
  },
  // Q25 — P-type, 2pts
  {
    text: 'Which TWO of the following requirements contain natural language defects? (Select two)',
    options: [
      '"The system shall display the account balance when the user opens the dashboard."',
      '"The processing of incoming data is handled in a timely manner."',
      '"The system shall send a confirmation email within 30 seconds of order placement."',
      '"Appropriate measures shall be taken to ensure system security."',
      '"The billing module shall generate monthly invoices on the first business day of each month."',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Option B contains a nominalization ("processing"), passive voice ("is handled"), and a vague term ("timely manner"). Option D contains a vague term ("appropriate measures") that is not measurable or testable. Options A, C, and E are clear, specific, and follow good sentence template practices.',
    chapter: 'Ch 5',
  },

  // ── Chapter 6: Model-Based Documentation (6 questions) ──
  // Q26 — A-type, 1pt
  {
    text: 'Refer to the diagram. Which statement about this use case diagram is correct?',
    diagram: 'graph LR\n  Customer((Customer))\n  Admin((Admin))\n  PaymentGW((Payment\\nGateway))\n  UC1[Place Order]\n  UC2[Manage Inventory]\n  UC3[Process Payment]\n  UC4[View Order History]\n  Customer --- UC1\n  Customer --- UC4\n  Admin --- UC2\n  UC1 -. "<<include>>" .-> UC3\n  PaymentGW --- UC3',
    options: [
      'The Payment Gateway is a use case that extends Place Order',
      'Place Order always includes Process Payment, and the Payment Gateway is an external actor',
      'Admin can place orders and manage inventory',
      'View Order History includes Process Payment',
    ],
    answer: 1,
    points: 1,
    explanation: 'The <<include>> relationship from "Place Order" to "Process Payment" means placing an order always incorporates payment processing. The Payment Gateway is an external system (actor) that participates in payment processing. Admin only manages inventory. View Order History has no relationship to Process Payment.',
    chapter: 'Ch 6',
  },
  // Q27 — A-type, 1pt
  {
    text: 'Refer to the diagram. In this state machine for an insurance claim, what must be true for a claim in the "Under Review" state to transition to "Approved"?',
    diagram: 'stateDiagram-v2\n  [*] --> Submitted\n  Submitted --> UnderReview : assign reviewer\n  UnderReview --> Approved : review complete [amount <= 10000]\n  UnderReview --> Escalated : review complete [amount > 10000]\n  Approved --> Paid : authorize payment\n  Escalated --> Approved : manager approval\n  Escalated --> Rejected : manager denial\n  Paid --> [*]\n  Rejected --> [*]',
    options: [
      'The review must be complete and the claim amount must be greater than 10,000',
      'The review must be complete and the claim amount must be 10,000 or less',
      'A manager must approve the claim regardless of the amount',
      'The claim must first pass through the Escalated state',
    ],
    answer: 1,
    points: 1,
    explanation: 'The transition from "Under Review" to "Approved" has the event "review complete" and the guard condition "[amount <= 10000]". Both must be satisfied: the review must be finished AND the amount must be 10,000 or less. Claims over 10,000 are escalated instead.',
    chapter: 'Ch 6',
  },
  // Q28 — A-type, 1pt
  {
    text: 'Refer to the diagram. What does this class diagram tell us about the relationship between Order and OrderItem?',
    diagram: 'classDiagram\n  class Customer {\n    +name: String\n    +email: String\n  }\n  class Order {\n    +orderDate: Date\n    +status: String\n    +calculateTotal(): Decimal\n  }\n  class OrderItem {\n    +quantity: Integer\n    +unitPrice: Decimal\n  }\n  class Product {\n    +name: String\n    +description: String\n  }\n  Customer "1" --> "0..*" Order : places\n  Order *-- "1..*" OrderItem : contains\n  OrderItem --> "1" Product : refers to',
    options: [
      'An Order can exist without any OrderItems',
      'OrderItems can exist independently without an Order',
      'An Order must contain at least one OrderItem, and OrderItems cannot exist without their Order (composition)',
      'The relationship between Order and OrderItem is a simple association with no ownership',
    ],
    answer: 2,
    points: 1,
    explanation: 'The filled diamond (*--) indicates composition: Order owns its OrderItems, and they cannot exist independently. The multiplicity "1..*" means an Order must have at least one OrderItem. If the Order is deleted, its OrderItems are also deleted. This is the classic composition example.',
    chapter: 'Ch 6',
  },
  // Q29 — K-type, 2pts
  {
    text: 'Which of the following statements about UML diagrams in requirements engineering are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'In a use case diagram, <<include>> means the included behavior is always executed as part of the base use case.', answer: true },
      { text: 'In a use case diagram, <<extend>> means the extending behavior is always executed as part of the base use case.', answer: false },
      { text: 'In a class diagram, a hollow diamond indicates aggregation, where parts can exist independently of the whole.', answer: true },
      { text: 'In an activity diagram, a fork node splits the flow into concurrent (parallel) paths.', answer: true },
    ],
    points: 2,
    explanation: '<<include>> is mandatory (always executed). <<extend>> is optional and conditional (only executed when an extension condition is met). Hollow diamond = aggregation (parts survive deletion of the whole). Fork nodes split flow into parallel paths that execute concurrently.',
    chapter: 'Ch 6',
  },
  // Q30 — K-type, 2pts
  {
    text: 'Which of the following statements about state machine diagrams are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A transition label follows the format: event [guard condition] / action.', answer: true },
      { text: 'A guard condition is a Boolean expression that must be true for the transition to fire.', answer: true },
      { text: 'A state machine diagram is best suited for modeling step-by-step business processes with parallel paths.', answer: false },
      { text: 'State machines model how an entity changes state in response to events over its lifecycle.', answer: true },
    ],
    points: 2,
    explanation: 'Transition labels follow the event [guard] / action format. Guards are Boolean conditions. State machines model entity lifecycle (e.g., an order going from New to Shipped to Delivered). Step-by-step processes with parallel paths are better modeled with activity diagrams, not state machines.',
    chapter: 'Ch 6',
  },
  // Q31 — P-type, 2pts
  {
    text: 'An RE needs to document both the data structure of a university enrollment domain AND the step-by-step enrollment workflow with parallel approval paths. Which TWO diagram types should be used? (Select two)',
    options: [
      'Class diagram — to show entities like Student, Course, and Enrollment with their attributes and relationships',
      'State machine diagram — to show the step-by-step enrollment workflow',
      'Activity diagram — to show the enrollment workflow including parallel approval paths (fork/join)',
      'Use case diagram — to show the data structure of the enrollment domain',
      'Goal model — to show the enrollment workflow steps',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'Class diagrams model data structure (entities, attributes, relationships). Activity diagrams model step-by-step workflows with decisions and parallel paths (fork/join). State machines model entity lifecycle, not workflows. Use case diagrams show functional overview, not data structure. Goal models capture motivation, not workflows.',
    chapter: 'Ch 6',
  },

  // ── Chapter 7: Validation & Negotiation (7 questions) ──
  // Q32 — A-type, 1pt
  {
    text: 'After writing the requirements specification for a new insurance claims system, the RE asks: "Do these requirements accurately reflect what the claims adjusters actually need?" This question represents:',
    options: [
      'Verification — checking that the code implements the specification correctly',
      'Validation — checking that the requirements match stakeholder intentions and needs',
      'Elicitation — gathering new requirements from the claims adjusters',
      'Management — tracking changes to the requirements baseline',
    ],
    answer: 1,
    points: 1,
    explanation: 'Validation asks "Are we building the right thing?" — it checks requirements against stakeholder needs and intentions. Verification asks "Are we building the thing right?" — it checks artifacts against specifications. This question checks if requirements match real needs, which is validation.',
    chapter: 'Ch 7',
  },
  // Q33 — A-type, 1pt
  {
    text: 'In a walkthrough, who leads the review session through the document?',
    options: [
      'An independent moderator who did not write the document',
      'The author of the document being reviewed',
      'The most senior developer in the team',
      'The project sponsor or client representative',
    ],
    answer: 1,
    points: 1,
    explanation: 'In a walkthrough, the AUTHOR leads the session, guiding reviewers through the document step by step. In an inspection, by contrast, an independent MODERATOR (who is NOT the author) leads the session. This distinction between walkthrough and inspection is a key IREB exam topic.',
    chapter: 'Ch 7',
  },
  // Q34 — A-type, 1pt
  {
    text: 'The marketing department wants a gamified onboarding experience with animations. The security team demands that all animations be disabled to prevent clickjacking attacks. What type of conflict is this?',
    options: [
      'Data conflict — they disagree about factual information',
      'Value conflict — they have different fundamental beliefs about what matters',
      'Structural conflict — the organizational structure causes the disagreement',
      'Interest conflict — they have incompatible goals driven by their departmental roles',
    ],
    answer: 3,
    points: 1,
    explanation: 'This is an interest conflict — both departments have legitimate but incompatible requirements driven by their different roles and interests (user engagement vs. security). It is not a data conflict (no factual disagreement), not a value conflict (not about fundamental beliefs), and not structural (not caused by organizational hierarchy).',
    chapter: 'Ch 7',
  },
  // Q35 — K-type, 2pts
  {
    text: 'Which of the following statements about validation techniques are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'An inspection is the most formal review technique, with defined roles including moderator, author, reviewers, and scribe.', answer: true },
      { text: 'In a walkthrough, an independent moderator leads the session, not the author.', answer: false },
      { text: 'Perspective-based reading involves reviewing requirements from different stakeholder viewpoints (user, developer, tester) to find gaps.', answer: true },
      { text: 'Prototyping for validation is useful when stakeholders cannot evaluate requirements presented only as abstract text.', answer: true },
    ],
    points: 2,
    explanation: 'Inspections are the most formal, with defined roles (moderator, author, reviewers, scribe). In a walkthrough the AUTHOR leads, not an independent moderator. Perspective-based reading uses different viewpoints to systematically find gaps. Prototyping helps stakeholders who need tangible representations to provide meaningful feedback.',
    chapter: 'Ch 7',
  },
  // Q36 — K-type, 2pts
  {
    text: 'Which of the following statements about conflict types and resolution are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A data conflict occurs when stakeholders disagree about facts, such as the number of expected users.', answer: true },
      { text: 'Consensus means all parties fully agree on the resolution without anyone compromising.', answer: true },
      { text: 'Overruling means a neutral third party facilitates the discussion to help stakeholders reach agreement.', answer: false },
      { text: 'Compromise means each party gives up something to reach a mutually acceptable solution.', answer: true },
    ],
    points: 2,
    explanation: 'Data conflicts are factual disagreements. Consensus means full agreement by all parties. Overruling means an authority figure decides unilaterally (not a neutral facilitator — that is mediation). Compromise means both sides make concessions.',
    chapter: 'Ch 7',
  },
  // Q37 — P-type, 2pts
  {
    text: 'Which TWO of the following are defined roles in a formal inspection according to IREB? (Select two)',
    options: [
      'Moderator — leads the review meeting and ensures the process is followed',
      'Developer — immediately fixes all defects found during the meeting',
      'Scribe — records all defects, decisions, and action items',
      'Project sponsor — decides which defects are worth fixing based on budget',
      'Tester — executes test cases against the document during the review',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'The four defined roles in an inspection are: moderator (leads the meeting), author (answers questions about the document), reviewer(s) (examine the document for defects), and scribe (records findings). Defects are NOT fixed during the meeting — rework happens afterward. There is no project sponsor or tester role in the inspection process.',
    chapter: 'Ch 7',
  },
  // Q38 — P-type, 1pt
  {
    text: 'Which TWO of the following are conflict resolution strategies identified by IREB? (Select two)',
    options: [
      'Avoidance — pretending the conflict does not exist',
      'Voting — the majority decision is adopted',
      'Escalation — sending the conflict to a higher court of law',
      'Mediation — a neutral third party helps stakeholders reach agreement',
      'Elimination — removing the conflicting stakeholders from the project',
    ],
    answer: [1, 3],
    multi: true,
    points: 1,
    explanation: 'IREB identifies five conflict resolution strategies: consensus, compromise, voting, overruling, and mediation. Voting uses majority decision. Mediation involves a neutral facilitator. Avoidance, legal escalation, and stakeholder elimination are not recognized IREB strategies.',
    chapter: 'Ch 7',
  },

  // ── Chapter 8: Requirements Management (6 questions) ──
  // Q39 — A-type, 1pt
  {
    text: 'A requirements engineer links Requirement R-42 to Business Goal BG-5 ("Reduce order processing time by 30%") and to Stakeholder Interview INT-12. What type of traceability is this?',
    options: [
      'Post-requirements traceability',
      'Inter-requirements traceability',
      'Pre-requirements traceability',
      'Bi-directional traceability',
    ],
    answer: 2,
    points: 1,
    explanation: 'Pre-requirements traceability links requirements BACKWARD to their sources — business goals, stakeholder interviews, regulations, and other origin artifacts. Post-requirements traceability links FORWARD to downstream artifacts (design, code, tests). Inter-requirements traceability links requirements to each other.',
    chapter: 'Ch 8',
  },
  // Q40 — A-type, 1pt
  {
    text: 'In the Kano model, a customer books a hotel room and finds complimentary champagne and chocolates waiting. This feature was not expected or requested. According to Kano, this is a:',
    options: [
      'Basic (must-be) requirement — expected by all customers',
      'Performance (linear) requirement — satisfaction increases with quality',
      'Excitement (delighter) requirement — not expected but creates strong satisfaction',
      'Indifferent requirement — customers do not care about it',
    ],
    answer: 2,
    points: 1,
    explanation: 'Excitement (delighter) requirements create strong positive reactions when present but are not missed when absent because customers did not expect them. Complimentary champagne is a surprise that delights. Basic requirements (e.g., clean room) are expected. Performance requirements (e.g., Wi-Fi speed) scale linearly with satisfaction.',
    chapter: 'Ch 8',
  },
  // Q41 — K-type, 2pts
  {
    text: 'Which of the following statements about requirements prioritization are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'MoSCoW classifies requirements into Must have, Should have, Could have, and Won\'t have.', answer: true },
      { text: 'Pairwise comparison requires N*(N-1)/2 comparisons, making it impractical for large requirement sets.', answer: true },
      { text: 'In the Kano model, basic (must-be) requirements cause high satisfaction when present.', answer: false },
      { text: 'Prioritization considers factors such as business value, risk, cost, and dependencies.', answer: true },
    ],
    points: 2,
    explanation: 'MoSCoW has four categories (Must/Should/Could/Won\'t). Pairwise comparison scales quadratically (N*(N-1)/2). In Kano, basic requirements are taken for granted when present (NOT high satisfaction) — they only cause dissatisfaction when absent. Prioritization considers multiple factors including value, risk, cost, and dependencies.',
    chapter: 'Ch 8',
  },
  // Q42 — K-type, 2pts
  {
    text: 'Which of the following statements about requirements management are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A requirements baseline is a formally agreed-upon snapshot of requirements at a specific point in time.', answer: true },
      { text: 'Once a baseline is established, no further changes to requirements are permitted.', answer: false },
      { text: 'The Change Control Board (CCB) evaluates and approves or rejects change requests.', answer: true },
      { text: 'A requirement attribute like "stability" indicates how likely the requirement is to change.', answer: true },
    ],
    points: 2,
    explanation: 'Baselines are frozen snapshots, but changes ARE still permitted — they must go through the formal change management process (change request, impact analysis, CCB decision, implementation, verification). The CCB evaluates changes. Stability is an attribute indicating change likelihood.',
    chapter: 'Ch 8',
  },
  // Q43 — P-type, 2pts
  {
    text: 'Which TWO of the following describe correct steps in the change management process? (Select two)',
    options: [
      'A change request is submitted and documented before any analysis begins.',
      'Changes are implemented immediately when a stakeholder verbally requests them, without documentation.',
      'An impact analysis identifies all artifacts (requirements, design, code, tests) affected by the change.',
      'The Change Control Board writes the source code for all approved changes.',
      'After approval, changes are implemented and then verified for correctness.',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'The change management process begins with a documented change request, followed by impact analysis (identifying all affected artifacts), CCB evaluation and decision, implementation, and verification. Changes should never be implemented without documentation. The CCB does not write code — it evaluates and decides.',
    chapter: 'Ch 8',
  },
  // Q44 — P-type, 2pts
  {
    text: 'Which TWO of the following are types of traceability defined by IREB? (Select two)',
    options: [
      'Pre-requirements traceability — linking requirements back to their sources (goals, stakeholders, regulations)',
      'Circular traceability — linking requirements in a loop back to themselves',
      'Post-requirements traceability — linking requirements forward to design, code, and test artifacts',
      'Temporal traceability — linking requirements to the calendar dates they were written',
      'Lateral traceability — linking requirements to requirements in other companies\' specifications',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'IREB defines three types: pre-requirements traceability (backward to sources), post-requirements traceability (forward to downstream artifacts), and inter-requirements traceability (between requirements). Circular, temporal, and lateral traceability are not defined IREB concepts.',
    chapter: 'Ch 8',
  },

  // ── Chapter 9: Tool Support (2 questions) ──
  // Q45 — A-type, 1pt
  {
    text: 'A small startup with five employees is choosing an RE tool. They have no established RE process and limited budget. An experienced consultant advises them: "A fool with a tool is still a fool." What does this principle mean?',
    options: [
      'Small teams should never use any tools for requirements engineering',
      'A tool cannot compensate for a poor or missing RE process — the process must be sound first',
      'Only expensive enterprise tools are effective for requirements engineering',
      'Tools should be selected before defining the RE process, so the tool can guide the process',
    ],
    answer: 1,
    points: 1,
    explanation: 'The "fool with a tool" principle means tools amplify existing processes — good or bad. An organization should first establish sound RE practices, then select tools that support those practices. A powerful tool will not fix a fundamentally broken or non-existent process.',
    chapter: 'Ch 9',
  },
  // Q46 — K-type, 2pts
  {
    text: 'Which of the following statements about RE tool support are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Dedicated RE tools (e.g., IBM DOORS, Jama Connect) support formal traceability, baselining, and change management.', answer: true },
      { text: 'General-purpose tools like spreadsheets and wikis are always sufficient for large regulated projects.', answer: false },
      { text: 'Tool selection should consider factors such as team size, project complexity, regulatory requirements, and integration needs.', answer: true },
      { text: 'Modeling tools help create and maintain UML diagrams and other visual requirement models.', answer: true },
    ],
    points: 2,
    explanation: 'Dedicated RE tools provide traceability, baselines, and change workflows. General-purpose tools lack these capabilities for large, regulated projects. Tool selection depends on context (team size, complexity, regulations, integrations). Modeling tools support UML and other visual notations.',
    chapter: 'Ch 9',
  },
]
</script>

# Sample Exam 1

<div class="exam-tip">
  <strong>Exam simulation:</strong> 46 questions, 70 points, 75-minute time limit, 70% passing score (49/70 pts). Includes single-select, pick-two, and True/False matrix questions — matching the real IREB CPRE-FL exam format.
</div>

<ExamQuiz :questions="questions" />
