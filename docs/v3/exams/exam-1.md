<script setup>
import ExamQuiz from '../../.vitepress/theme/ExamQuiz.vue'

const questions = [
  // ── EU 1: Introduction and Overview (3 questions, 4 pts) ──
  // Q1 — A-type, 1pt
  {
    text: 'What is the goal of Requirements Engineering according to the syllabus?',
    options: [
      'To design the system architecture based on stakeholder interviews',
      'To specify and manage requirements so that the implemented system satisfies stakeholders\' desires and needs',
      'To create a project plan that includes all development milestones',
      'To test the system against documented acceptance criteria',
    ],
    answer: 1,
    points: 1,
    explanation: 'The goal of RE is to specify and manage requirements for systems such that the systems implemented and deployed satisfy their stakeholders\' desires and needs.',
    chapter: 'EU 1',
  },
  // Q2 — A-type, 1pt
  {
    text: 'Which of the following is a typical symptom of inadequate Requirements Engineering?',
    options: [
      'Too many stakeholders identified early in the project',
      'Rushing straight into building the system without eliciting requirements',
      'Using iterative development instead of a linear process',
      'Having a dedicated Requirements Engineer on the team',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus lists four symptoms: rushing into building, communication problems, assuming requirements are self-evident, and inadequate RE education and skills.',
    chapter: 'EU 1',
  },
  // Q3 — K-type, 2pts
  {
    text: 'Which of the following statements about Requirements Engineering are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Functional requirements concern a result or behavior to be provided by a function of the system.', answer: true },
      { text: 'Quality requirements pertain to quality concerns not covered by functional requirements, such as performance and security.', answer: true },
      { text: 'Constraints expand the solution space to allow more creative approaches.', answer: false },
      { text: 'Requirements Engineer is typically a job title, not a role.', answer: false },
    ],
    points: 2,
    explanation: 'Functional requirements concern behavior/results; quality requirements cover concerns like performance and security. Constraints LIMIT (not expand) the solution space. Requirements Engineer is typically a role (not a job title) played by BAs, product owners, developers, etc.',
    chapter: 'EU 1',
  },

  // ── EU 2: Fundamental Principles (4 questions, 6 pts) ──
  // Q4 — A-type, 1pt
  {
    text: 'According to the principle "Value orientation," the value of a requirement equals:',
    options: [
      'The number of stakeholders who requested it',
      'Its benefit minus the cost for eliciting, documenting, validating, and managing it',
      'The effort required to implement it in the system',
      'The priority assigned by the product owner',
    ],
    answer: 1,
    points: 1,
    explanation: 'The value of a requirement is equal to its benefit (contribution to satisfying stakeholders and reducing risk) minus the cost for eliciting, documenting, validating, and managing it.',
    chapter: 'EU 2',
  },
  // Q5 — A-type, 1pt
  {
    text: 'The principle "Innovation" states that good RE strives to:',
    options: [
      'Use the most advanced modeling languages available',
      'Automate all elicitation activities using AI',
      'Satisfy stakeholders\' needs better than they expect, not just give them exactly what they want',
      'Always adopt the newest development framework',
    ],
    answer: 2,
    points: 1,
    explanation: 'The principle states: giving stakeholders exactly what they want misses the opportunity to build systems that satisfy their needs better than they expect. Good RE strives to make stakeholders happy, excited, or feel safe.',
    chapter: 'EU 2',
  },
  // Q6 — K-type, 2pts
  {
    text: 'Which of the following statements about the nine fundamental principles of RE are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Shared understanding has two forms: explicit (documented and agreed) and implicit (shared knowledge about needs and context).', answer: true },
      { text: 'The principle "Context" states that the system boundary is always fixed and cannot change over time.', answer: false },
      { text: 'The principle "Evolution" means that changing requirements are no accident, but the normal case.', answer: true },
      { text: 'Systematic and disciplined work means always using the same process and set of practices.', answer: false },
    ],
    points: 2,
    explanation: 'Shared understanding has explicit and implicit forms. The system boundary is initially often NOT clear and may change. Changing requirements ARE normal. Systematic work means adapting processes to the situation — NOT always using the same ones.',
    chapter: 'EU 2',
  },
  // Q7 — K-type, 2pts
  {
    text: 'Which of the following statements about the principle "Problem – Requirement – Solution" are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Problems, requirements, and solutions are closely intertwined and cannot be tackled in isolation.', answer: true },
      { text: 'Problems, requirements, and solutions must always occur in this strict sequence.', answer: false },
      { text: 'Solution ideas may create user needs which then become requirements.', answer: true },
      { text: 'Requirements Engineers aim to separate problems, requirements, and solutions when thinking, communicating, and documenting.', answer: true },
    ],
    points: 2,
    explanation: 'The three are intertwined but do NOT necessarily occur in a fixed order. Solution ideas can create needs (especially when innovating). Despite being intertwined, REs aim to separate them as far as possible — this separation of concerns makes RE tasks easier.',
    chapter: 'EU 2',
  },

  // ── EU 3: Work Products and Documentation (18 questions, 30 pts) ──
  // Q8 — A-type, 1pt
  {
    text: 'Which of the following is NOT a characteristic used to describe a work product?',
    options: [
      'Purpose',
      'Representation',
      'Cost',
      'Life span',
    ],
    answer: 2,
    points: 1,
    explanation: 'Work products are characterized by their purpose, representation, size, and life span. Cost is not listed as a characteristic.',
    chapter: 'EU 3',
  },
  // Q9 — A-type, 1pt
  {
    text: 'A product backlog with user stories that is continuously updated and refined is an example of which type of work product by life span?',
    options: [
      'Temporary',
      'Evolving',
      'Durable',
      'Static',
    ],
    answer: 1,
    points: 1,
    explanation: 'Evolving work products emerge over several iterations and need some metadata. A product backlog that is continuously refined is a classic example of an evolving work product.',
    chapter: 'EU 3',
  },
  // Q10 — K-type, 2pts
  {
    text: 'Which of the following statements about abstraction levels and level of detail in work products are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Requirements on different levels of abstraction should not be mixed in small work products.', answer: true },
      { text: 'Greater level of detail always results in lower cost of the specification.', answer: false },
      { text: 'The level of detail depends on factors such as shared understanding and cost vs. value.', answer: true },
      { text: 'A high-level requirement may be refined into several detailed requirements at lower levels.', answer: true },
    ],
    points: 2,
    explanation: 'Do not mix abstraction levels. Greater detail INCREASES cost (but reduces risk). Level of detail depends on context, shared understanding, cost vs. value, etc. Refinement from high to low abstraction is standard practice.',
    chapter: 'EU 3',
  },
  // Q11 — K-type, 2pts
  {
    text: 'Which of the following are general documentation guidelines according to the syllabus?',
    type: 'ktype',
    statements: [
      { text: 'Select a work product type that fits the intended purpose.', answer: true },
      { text: 'Repeat information across work products to ensure completeness.', answer: false },
      { text: 'Use terms consistently as defined in the glossary.', answer: true },
      { text: 'Structure work products appropriately.', answer: true },
    ],
    points: 2,
    explanation: 'The guidelines say to avoid redundancy by referencing content instead of repeating it. Selecting fitting types, using consistent terms, and structuring appropriately are all correct guidelines.',
    chapter: 'EU 3',
  },
  // Q12 — P-type, 2pts
  {
    text: 'Which TWO of the following are quality criteria for single requirements? (Select two)',
    options: [
      'Adequate (describes true and agreed stakeholder needs)',
      'Consistent (no contradictions with other requirements)',
      'Verifiable',
      'Traceable',
      'Modifiable',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'Quality criteria for SINGLE requirements are: adequate, necessary, unambiguous, complete, understandable, verifiable. Consistent, traceable, and modifiable are criteria for WORK PRODUCTS containing multiple requirements.',
    chapter: 'EU 3',
  },
  // Q13 — A-type, 1pt
  {
    text: 'What is the main disadvantage of natural-language-based work products?',
    options: [
      'They require specialized training to read',
      'They cannot express quality requirements',
      'Texts can frequently be interpreted in different ways',
      'They are too formal for most stakeholders',
    ],
    answer: 2,
    points: 1,
    explanation: 'The main disadvantage is ambiguity — natural-language texts can frequently be interpreted in different ways. Detection of ambiguities, omissions, and inconsistencies is difficult and expensive.',
    chapter: 'EU 3',
  },
  // Q14 — K-type, 2pts
  {
    text: 'Which of the following statements about natural-language pitfalls are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Incomplete descriptions should be avoided in requirements.', answer: true },
      { text: 'Passive voice should always be avoided and is listed as a "thing to avoid."', answer: false },
      { text: 'Nominalizations (nouns derived from verbs) are listed as "things to be used with care."', answer: true },
      { text: 'Universal quantifiers like "all" or "never" should be used with care.', answer: true },
    ],
    points: 2,
    explanation: 'Incomplete descriptions are "things to avoid." Passive voice and nominalizations are "things to USE WITH CARE" (not avoid entirely). Universal quantifiers are also "use with care."',
    chapter: 'EU 3',
  },
  // Q15 — A-type, 1pt
  {
    text: 'A predefined syntactic structure for expressing an individual requirement (e.g., "The <system> shall <verb> <object>") is called a:',
    options: [
      'Form template',
      'Document template',
      'Phrase template',
      'Specification pattern',
    ],
    answer: 2,
    points: 1,
    explanation: 'A phrase template provides a predefined syntactic structure for expressing an individual requirement or user story. Form templates provide fields in a form. Document templates structure a whole document.',
    chapter: 'EU 3',
  },
  // Q16 — P-type, 2pts
  {
    text: 'Which TWO are advantages of template-based work products? (Select two)',
    options: [
      'They eliminate all ambiguity from requirements',
      'They provide a clear, re-usable structure',
      'They guarantee that no requirements are missed',
      'They help to capture the most relevant information',
      'They automatically detect inconsistencies',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Templates provide clear, re-usable structure and help capture the most relevant information. They do NOT eliminate all ambiguity, guarantee completeness, or automatically detect inconsistencies.',
    chapter: 'EU 3',
  },
  // Q17 — K-type, 2pts
  {
    text: 'Which of the following statements about glossaries are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A glossary should be managed centrally and maintained over the entire development.', answer: true },
      { text: 'Synonyms (different terms for the same thing) should be marked in the glossary.', answer: true },
      { text: 'The use of the glossary should be optional to avoid slowing down stakeholders.', answer: false },
      { text: 'Homonyms (same term for different things) should be avoided or marked.', answer: true },
    ],
    points: 2,
    explanation: 'The glossary rules state it should be managed centrally, maintained throughout development, and its use should be MANDATORY (not optional). Synonyms should be marked, and homonyms should be avoided or marked.',
    chapter: 'EU 3',
  },
  // Q18 — A-type, 1pt
  {
    text: 'A model is described in the syllabus as:',
    options: [
      'A complete and detailed replica of the system to be built',
      'An abstract representation of an existing or to-be-created part of reality',
      'A working prototype that users can interact with',
      'A list of all requirements organized by priority',
    ],
    answer: 1,
    points: 1,
    explanation: 'A model is an abstract representation of an existing part of reality or a part of reality to be created. It focuses on some aspects while abstracting from others.',
    chapter: 'EU 3',
  },
  // Q19 — K-type, 2pts
  {
    text: 'Which of the following statements about the role of models in RE are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Models help understand relationships and interconnections between requirements.', answer: true },
      { text: 'Models can fully replace natural-language requirements in all situations.', answer: false },
      { text: 'Modeling languages have a restricted syntax which reduces possible ambiguities.', answer: true },
      { text: 'Models focus primarily on functional requirements.', answer: true },
    ],
    points: 2,
    explanation: 'Models help with relationships and reduce ambiguity through restricted syntax, but they focus primarily on functional requirements. Most quality requirements and constraints cannot be expressed in models, so they CANNOT fully replace natural language in all situations.',
    chapter: 'EU 3',
  },
  // Q20 — P-type, 2pts
  {
    text: 'Which TWO are uses of models in RE according to the syllabus? (Select two)',
    options: [
      'Replacing the requirements management process',
      'Decomposing complex reality into well-defined, complementing aspects',
      'Automatically generating source code from requirements',
      'Validating textual requirements to uncover omissions and inconsistencies',
      'Replacing stakeholder interviews during elicitation',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'The syllabus lists four uses: specifying functional requirements, decomposing complex reality into aspects, paraphrasing textual requirements, and validating textual requirements to find omissions, ambiguities, and inconsistencies.',
    chapter: 'EU 3',
  },
  // Q21 — A-type, 1pt
  {
    text: 'In a UML class diagram, what does a hollow diamond at one end of an association represent?',
    options: [
      'Composition — the part cannot exist without the whole',
      'Aggregation — the part can exist independently of the whole',
      'Generalization — inheritance between classes',
      'Dependency — one class depends on another',
    ],
    answer: 1,
    points: 1,
    explanation: 'A hollow diamond represents aggregation (weak "has-a") where the part can exist independently. A filled diamond represents composition (strong "has-a") where the part cannot exist without the whole.',
    chapter: 'EU 3',
  },
  // Q22 — K-type, 2pts
  {
    text: 'Which of the following statements about UML activity diagrams are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A fork element splits a single flow into multiple concurrent parallel flows.', answer: true },
      { text: 'A decision element (diamond) represents a point where the flow branches based on a condition.', answer: true },
      { text: 'Swim lanes show which actor is responsible for which action.', answer: true },
      { text: 'Activity diagrams can only be used for software processes, not business processes.', answer: false },
    ],
    points: 2,
    explanation: 'Fork splits into parallel flows, diamonds represent decisions, swim lanes show responsibility. Activity diagrams can be used for BOTH software functions and business processes.',
    chapter: 'EU 3',
  },
  // Q23 — K-type, 2pts
  {
    text: 'Which of the following statements about prototypes in RE are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Wireframes are low-fidelity exploratory prototypes built with simple materials or sketching tools.', answer: true },
      { text: 'Evolutionary prototypes are discarded after use, unlike exploratory prototypes.', answer: false },
      { text: 'Mock-ups are medium-fidelity prototypes that use real screens but without real functionality.', answer: true },
      { text: 'Prototypes can be used to validate requirements.', answer: true },
    ],
    points: 2,
    explanation: 'Wireframes are low-fidelity; mock-ups are medium-fidelity. EXPLORATORY prototypes are discarded after use, not evolutionary ones. Evolutionary prototypes are pilot systems that evolve into the final product. Prototypes are indeed used for validation.',
    chapter: 'EU 3',
  },
  // Q24 — P-type, 2pts
  {
    text: 'Which TWO are quality criteria for work products containing multiple requirements (not for single requirements)? (Select two)',
    options: [
      'Unambiguous',
      'Consistent',
      'Adequate',
      'Non-redundant',
      'Verifiable',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Quality criteria for WORK PRODUCTS (multiple requirements): consistent, non-redundant, complete, modifiable, traceable, conformant. Unambiguous, adequate, and verifiable are criteria for SINGLE requirements.',
    chapter: 'EU 3',
  },
  // Q25 — A-type, 1pt
  {
    text: 'A UML state machine diagram transition has the form "event [guard] / action." What is the guard?',
    options: [
      'The event that triggers the transition',
      'The action performed when the transition fires',
      'A boolean condition that must be true for the transition to occur',
      'The name of the target state',
    ],
    answer: 2,
    points: 1,
    explanation: 'In a state machine transition, the guard is a boolean condition (in square brackets) that must be true for the transition to occur. The event triggers it, the action is what happens.',
    chapter: 'EU 3',
  },

  // ── EU 4: Practices for Elaboration (10 questions, 14 pts) ──
  // Q26 — A-type, 1pt
  {
    text: 'What are the three types of requirements sources classified by the syllabus?',
    options: [
      'Internal sources, external sources, and regulatory sources',
      'Stakeholders, documents, and systems',
      'Users, testers, and developers',
      'Primary sources, secondary sources, and tertiary sources',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus classifies requirements sources into three types: stakeholders (the main source), documents (regulations, process docs), and systems (existing/legacy systems).',
    chapter: 'EU 4',
  },
  // Q27 — A-type, 1pt
  {
    text: 'In the Kano model, which category of requirements describes features that are NOT expected but cause strong satisfaction when present?',
    options: [
      'Dissatisfiers (basic factors)',
      'Satisfiers (performance factors)',
      'Delighters (excitement factors)',
      'Constraints',
    ],
    answer: 2,
    points: 1,
    explanation: 'Delighters (excitement factors, unconscious requirements) are not expected by stakeholders. Their presence causes strong satisfaction, but their absence is not noticed since they were never expected.',
    chapter: 'EU 4',
  },
  // Q28 — A-type, 1pt
  {
    text: 'Which quality model does the syllabus recommend as a checklist for eliciting quality requirements?',
    options: [
      'CMMI',
      'ISO 25010',
      'TOGAF',
      'Six Sigma',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus recommends using a quality model such as ISO 25010 as a checklist for eliciting quality requirements. It can also help in quantifying requirements.',
    chapter: 'EU 4',
  },
  // Q29 — K-type, 2pts
  {
    text: 'Which of the following statements about elicitation techniques are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Gathering techniques help elicit satisfiers and dissatisfiers by investigating different sources.', answer: true },
      { text: 'Design and idea-generating techniques aim to create ideas that may lead to delighters.', answer: true },
      { text: 'A single elicitation technique is always sufficient for a project.', answer: false },
      { text: 'Brainstorming and prototyping are examples of design and idea-generating techniques.', answer: true },
    ],
    points: 2,
    explanation: 'Gathering techniques target satisfiers/dissatisfiers. Design techniques target delighters. The best results come from COMBINING techniques — no single technique suffices. Brainstorming and prototyping are design/idea-generating techniques.',
    chapter: 'EU 4',
  },
  // Q30 — A-type, 1pt
  {
    text: 'Which of the following is NOT a conflict type listed in the syllabus?',
    options: [
      'Subject matter conflict',
      'Budget conflict',
      'Value conflict',
      'Structural conflict',
    ],
    answer: 1,
    points: 1,
    explanation: 'The six conflict types are: subject matter, data, interest, value, relationship, and structural. "Budget conflict" is not specifically listed.',
    chapter: 'EU 4',
  },
  // Q31 — K-type, 2pts
  {
    text: 'Which of the following statements about requirements validation are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Validation should involve the right stakeholders.', answer: true },
      { text: 'Identification and correction of defects should be done simultaneously in a single step.', answer: false },
      { text: 'Validation should be performed from different views.', answer: true },
      { text: 'Validation should be repeated at multiple points, not just once.', answer: true },
    ],
    points: 2,
    explanation: 'The four important aspects: involve the right stakeholders, SEPARATE identification from correction of defects, validate from different views, and repeat validation. Identification and correction should NOT be simultaneous.',
    chapter: 'EU 4',
  },
  // Q32 — A-type, 1pt
  {
    text: 'Which conflict resolution technique involves a person with authority making the decision?',
    options: [
      'Agreement',
      'Compromise',
      'Voting',
      'Overruling',
    ],
    answer: 3,
    points: 1,
    explanation: 'Overruling means a person with authority makes the decision. Agreement = all parties reach a shared decision. Compromise = each party gives up something. Voting = democratic majority decision.',
    chapter: 'EU 4',
  },
  // Q33 — K-type, 2pts
  {
    text: 'Which of the following statements about stakeholders and stakeholder management are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Stakeholder identification should take place at the beginning and be managed as a continuous activity.', answer: true },
      { text: 'It is sufficient to consider only end users as stakeholders.', answer: false },
      { text: 'When end users cannot be individually identified, personas can be defined as substitutes.', answer: true },
      { text: 'A stakeholder may have more than one role at the same time.', answer: true },
    ],
    points: 2,
    explanation: 'Stakeholder identification is continuous, not one-time. Considering ONLY end users would miss critical requirements from other stakeholders. Personas substitute for unidentifiable individuals. Stakeholders can have multiple roles simultaneously.',
    chapter: 'EU 4',
  },
  // Q34 — A-type, 1pt
  {
    text: 'Walkthroughs and inspections are examples of which category of validation technique?',
    options: [
      'Exploratory techniques',
      'Review techniques',
      'Analytical techniques',
      'Statistical techniques',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus classifies validation techniques into review techniques (walkthroughs, inspections) and exploratory techniques (prototyping, alpha/beta testing, A/B testing, MVP, sample development).',
    chapter: 'EU 4',
  },
  // Q35 — A-type, 1pt
  {
    text: 'The four subcategories of gathering techniques are:',
    options: [
      'Planning, execution, review, and closure techniques',
      'Questioning, collaboration, observation, and artifact-based techniques',
      'Interview, workshop, survey, and prototyping techniques',
      'Individual, group, documentary, and experimental techniques',
    ],
    answer: 1,
    points: 1,
    explanation: 'The four subcategories of gathering techniques are: questioning techniques, collaboration techniques, observation techniques, and artifact-based techniques.',
    chapter: 'EU 4',
  },

  // ── EU 5: Process and Working Structure (2 questions, 3 pts) ──
  // Q36 — A-type, 1pt
  {
    text: 'Which of the following is a criterion for choosing an iterative RE process?',
    options: [
      'The stakeholders know their requirements and can specify them up front',
      'A comprehensive requirements specification is required for a contract',
      'Many requirements are not known up front but will emerge during development',
      'Regulatory authorities require a formally released specification early on',
    ],
    answer: 2,
    points: 1,
    explanation: 'An iterative process is suitable when many requirements are not known up front. The other options are all criteria for choosing a LINEAR RE process.',
    chapter: 'EU 5',
  },
  // Q37 — K-type, 2pts
  {
    text: 'Which of the following statements about RE process facets are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'In a prescriptive RE process, the requirements specification constitutes a contract.', answer: true },
      { text: 'Explorative RE processes are typically also iterative.', answer: true },
      { text: 'The market-oriented facet combines well with the linear and prescriptive facets.', answer: false },
      { text: 'In a customer-specific process, individual persons can typically be identified for stakeholder roles.', answer: true },
    ],
    points: 2,
    explanation: 'Prescriptive = contract-based, all requirements binding. Explorative and iterative typically go together. Market-oriented does NOT combine well with linear/prescriptive. In customer-specific processes, individual stakeholders are typically identifiable.',
    chapter: 'EU 5',
  },

  // ── EU 6: Management Practices (6 questions, 10 pts) ──
  // Q38 — A-type, 1pt
  {
    text: 'What is the purpose of a requirements life cycle model?',
    options: [
      'To define the overall project timeline and milestones',
      'To define allowed statuses and state transitions for work products',
      'To specify the order in which requirements are implemented',
      'To document the cost of each change request',
    ],
    answer: 1,
    points: 1,
    explanation: 'A life cycle model defines allowed statuses and state transitions for work products, so the current state is always clear, including the transition history.',
    chapter: 'EU 6',
  },
  // Q39 — K-type, 2pts
  {
    text: 'Which of the following statements about version control and baselines are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Version control requires a version number, a change history, and a storage concept.', answer: true },
      { text: 'A baseline is a stable, change-controlled configuration used for release planning.', answer: true },
      { text: 'Once a work product is baselined, its configuration can be freely modified.', answer: false },
      { text: 'A requirements configuration contains at most one version of each work product.', answer: true },
    ],
    points: 2,
    explanation: 'Version control needs three things: version number, change history, storage concept. A baseline IS stable and change-controlled. Once baselined, the configuration is UNCHANGEABLE (not freely modifiable). A configuration contains at most one version of each work product.',
    chapter: 'EU 6',
  },
  // Q40 — P-type, 2pts
  {
    text: 'Which TWO are types of views on requirements according to the syllabus? (Select two)',
    options: [
      'Selective views',
      'Historical views',
      'Aggregating views',
      'Predictive views',
      'Hierarchical views',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'The three types of views are: selective (filter by attribute values), projective (show specific attributes), and aggregating (summarize across requirements). Historical, predictive, and hierarchical are not listed.',
    chapter: 'EU 6',
  },
  // Q41 — K-type, 2pts
  {
    text: 'Which of the following statements about traceability are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Traceability is the ability to trace a requirement back to its origin and forward to subsequent work products.', answer: true },
      { text: 'Implicit traceability is achieved by structuring and standardizing work products.', answer: true },
      { text: 'Explicit traceability relates work products using unique identifiers.', answer: true },
      { text: 'Traceability is only needed in regulated industries and can be skipped in agile projects.', answer: false },
    ],
    points: 2,
    explanation: 'Traceability goes backward (to sources) and forward (to test cases, etc.). Implicit traceability uses structure/standards. Explicit uses unique identifiers. Traceability is a prerequisite for requirements management regardless of methodology — it is often demanded by standards and regulations.',
    chapter: 'EU 6',
  },
  // Q42 — A-type, 1pt
  {
    text: 'In an agile approach, how are requirements changes typically handled?',
    options: [
      'A Change Control Board evaluates and approves each change',
      'Changes are rejected after the initial sprint planning',
      'The product owner includes the change in the product backlog and prioritizes it',
      'The development team votes on whether to accept the change',
    ],
    answer: 2,
    points: 1,
    explanation: 'In an iterative/agile approach, the product owner includes the change in the product backlog and prioritizes the new item accordingly. In a linear approach, a Change Control Board typically decides.',
    chapter: 'EU 6',
  },
  // Q43 — K-type, 2pts
  {
    text: 'Which of the following statements about prioritization are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Not all requirements are equally important.', answer: true },
      { text: 'Prioritization techniques are classified into ad-hoc and analytical techniques.', answer: true },
      { text: 'Prioritization should only consider a single criterion such as business value.', answer: false },
      { text: 'Steps for prioritization include defining goals, assessment criteria, stakeholders, and the requirements to be prioritized.', answer: true },
    ],
    points: 2,
    explanation: 'Requirements vary in importance. Techniques are ad-hoc or analytical. Prioritization can be based on MULTIPLE criteria (business value, urgency, effort, dependencies). The steps include defining goals, criteria, stakeholders, requirements, selecting a technique, and performing it.',
    chapter: 'EU 6',
  },

  // ── EU 7: Tool Support (2 questions, 3 pts) ──
  // Q44 — A-type, 1pt
  {
    text: 'According to the syllabus, what should be established BEFORE selecting an RE tool?',
    options: [
      'The budget for tool licenses',
      'The number of users who will access the tool',
      'Proper RE procedures and techniques',
      'The programming language of the system under development',
    ],
    answer: 2,
    points: 1,
    explanation: 'An appropriate tool can only be sought once proper RE procedures and techniques have been introduced. Tool introduction requires clear RE responsibilities and procedures — the tool supports the process, not the other way around.',
    chapter: 'EU 7',
  },
  // Q45 — K-type, 2pts
  {
    text: 'Which of the following statements about RE tool support are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'RE tools can support management of requirements, management of the RE process, and documentation of knowledge.', answer: true },
      { text: 'A single RE tool typically supports all RE activities comprehensively.', answer: false },
      { text: 'General-purpose tools like spreadsheets should only be used when the RE process is in control and requirements are stable.', answer: true },
      { text: 'When introducing a tool, pilot projects should be used to avoid risks.', answer: true },
    ],
    points: 2,
    explanation: 'Three categories of tool support exist. Tools rarely support ALL activities — different tools may need to be combined. General-purpose tools have limitations and should only be used when RE is in control. Pilot projects help avoid adoption risks.',
    chapter: 'EU 7',
  },
]
</script>

# Sample Exam 1 (Syllabus v3.3.0)

::: info Official Practice Exam
The official IREB practice exam is free and available in 12 languages: [Download from IREB](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

<div class="exam-tip">
  <strong>Exam simulation:</strong> 45 questions, 70 points, 75-minute time limit, 70% passing score (49/70 pts). Covers all 7 Educational Units in the official format — single-select (A-type), pick-two (P-type), and true/false matrix (K-type) questions.
</div>

<ExamQuiz :questions="questions" />
