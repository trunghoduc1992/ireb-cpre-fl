<script setup>
import ExamQuiz from '../.vitepress/theme/ExamQuiz.vue'

const questions = [
  // ── EU 1: Introduction and Overview (3 questions, 4 pts) ──
  // Q1 — K-type, 2pts
  {
    text: 'Which of the following statements about Requirements Engineering are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'RE distinguishes three kinds of requirements: functional requirements, quality requirements, and constraints.', answer: true },
      { text: 'Quality requirements pertain to concerns such as performance, availability, and security.', answer: true },
      { text: 'RE can only be applied to software systems, not to products or services.', answer: false },
      { text: 'The major tasks in RE are elicitation, documentation, validation, and management.', answer: true },
    ],
    points: 2,
    explanation: 'Three kinds of requirements are correct. Quality requirements cover performance, availability, security, etc. RE can be applied to ANY kind of system (products, services, devices). The four major tasks are correct.',
    chapter: 'EU 1',
  },
  // Q2 — A-type, 1pt
  {
    text: 'Which of the following best describes the term "stakeholder" in the context of RE?',
    options: [
      'A person who funds the project',
      'A person or organization who influences the requirements or is impacted by the system',
      'A developer who implements the requirements',
      'A tester who validates the system against requirements',
    ],
    answer: 1,
    points: 1,
    explanation: 'Stakeholders are persons or organizations who influence the requirements for a system or who are impacted by that system. This is broader than just sponsors, developers, or testers.',
    chapter: 'EU 1',
  },
  // Q3 — A-type, 1pt
  {
    text: 'Which of the following describes how requirements can occur?',
    options: [
      'Only as system requirements',
      'Only as user requirements and business requirements',
      'As system, stakeholder, user, domain, and business requirements',
      'Only as functional and non-functional requirements',
    ],
    answer: 2,
    points: 1,
    explanation: 'The syllabus lists five levels: system requirements, stakeholder requirements, user requirements, domain requirements, and business requirements.',
    chapter: 'EU 1',
  },

  // ── EU 2: Fundamental Principles (4 questions, 6 pts) ──
  // Q4 — K-type, 2pts
  {
    text: 'Which of the following statements about the nine fundamental principles are true and which are false?',
    type: 'ktype',
    statements: [
      { text: '"Value orientation" means the value of a requirement equals its benefit minus the cost of handling it.', answer: true },
      { text: '"Validation" means non-validated requirements are useless.', answer: true },
      { text: '"Stakeholders" means it is sufficient to consider only end users for requirements.', answer: false },
      { text: '"Evolution" means changing requirements are an accident that should be prevented.', answer: false },
    ],
    points: 2,
    explanation: 'Value orientation: benefit minus cost is correct. Non-validated requirements ARE useless. It is NOT sufficient to consider only end users — other stakeholders may have critical requirements. Evolution: changing requirements are NO accident, but the NORMAL case.',
    chapter: 'EU 2',
  },
  // Q5 — A-type, 1pt
  {
    text: 'Which practice does the syllabus identify as "the most important" for reducing the impact of misunderstandings?',
    options: [
      'Creating detailed requirements specifications',
      'Using a process with short feedback loops',
      'Conducting formal inspections of all documents',
      'Assigning a dedicated Requirements Engineer',
    ],
    answer: 1,
    points: 1,
    explanation: 'Under Principle 3 (Shared Understanding), the syllabus states: "The most important practice for reducing the impact of misunderstandings is using a process with short feedback loops."',
    chapter: 'EU 2',
  },
  // Q6 — A-type, 1pt
  {
    text: 'The principle "Context" introduces three boundaries/concepts. Which of the following is NOT one of them?',
    options: [
      'System boundary',
      'Context boundary',
      'Solution boundary',
      'System context',
    ],
    answer: 2,
    points: 1,
    explanation: 'Principle 4 introduces: the system boundary (between system and context), the context boundary (between relevant and irrelevant environment), and the system context (the relevant part of the environment). "Solution boundary" is not a concept in this principle.',
    chapter: 'EU 2',
  },
  // Q7 — K-type, 2pts
  {
    text: 'Which of the following statements about the principle "Systematic and disciplined work" are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A systematic approach to RE improves quality even in ad-hoc development.', answer: true },
      { text: 'Requirements Engineers should always re-use processes from past successful work.', answer: false },
      { text: 'Processes, practices, and work products must be chosen to fit the specific situation.', answer: true },
      { text: 'There is a single process in RE that works well in most situations.', answer: false },
    ],
    points: 2,
    explanation: 'Systematic RE helps even in ad-hoc settings. REs should NOT blindly re-use past processes without reflection. Choices must fit the situation. There is NO single process that works in most situations.',
    chapter: 'EU 2',
  },

  // ── EU 3: Work Products and Documentation (18 questions, 30 pts) ──
  // Q8 — A-type, 1pt
  {
    text: 'User stories, individual requirements, and user needs are examples of work products for:',
    options: [
      'A coherent set of requirements',
      'A single requirement',
      'A comprehensive document',
      'A glossary entry',
    ],
    answer: 1,
    points: 1,
    explanation: 'Work products for a single requirement include individual requirements and user stories. Use cases and graphic models are for coherent sets. System requirements specifications and backlogs are comprehensive documents.',
    chapter: 'EU 3',
  },
  // Q9 — K-type, 2pts
  {
    text: 'Which of the following statements about work product life spans are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Temporary work products are created to support communication and shared understanding.', answer: true },
      { text: 'Durable work products have been baselined or released and need a full set of metadata.', answer: true },
      { text: 'A temporary work product can never become a durable work product.', answer: false },
      { text: 'Change control must be followed for durable work products.', answer: true },
    ],
    points: 2,
    explanation: 'Temporary work products support communication. Durable ones are baselined/released with full metadata and change control. A temporary work product CAN become durable by being baselined or released.',
    chapter: 'EU 3',
  },
  // Q10 — A-type, 1pt
  {
    text: 'Which aspect of work products focuses on "structure and data, function and flow, state and behavior"?',
    options: [
      'The kind of requirement (functional, quality, constraint)',
      'The functional aspects of requirements',
      'The context aspects',
      'The documentation guidelines',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus lists three aspects: kind (functional, quality, constraint), functional aspects (structure/data, function/flow, state/behavior), and context aspects (system context, system boundary).',
    chapter: 'EU 3',
  },
  // Q11 — P-type, 2pts
  {
    text: 'Which TWO are advantages of natural-language-based work products? (Select two)',
    options: [
      'They are always unambiguous and precise',
      'They are extremely expressive and flexible',
      'Almost any requirement can be expressed in natural language',
      'Detection of omissions and inconsistencies is easy',
      'They enforce a consistent structure',
    ],
    answer: [1, 2],
    multi: true,
    points: 2,
    explanation: 'Natural language is extremely expressive/flexible and can express almost any requirement. However, it is prone to ambiguity (not always precise), detection of issues is DIFFICULT (not easy), and it does not enforce structure.',
    chapter: 'EU 3',
  },
  // Q12 — K-type, 2pts
  {
    text: 'Which of the following statements about writing natural-language requirements are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Writing short and well-structured sentences supports good requirements.', answer: true },
      { text: 'Unspecific nouns are a "thing to avoid" in requirements.', answer: true },
      { text: 'Incomplete comparisons (e.g., "the system shall be faster") are acceptable.', answer: false },
      { text: 'Using a uniform terminology defined in a glossary helps reduce ambiguity.', answer: true },
    ],
    points: 2,
    explanation: 'Short sentences, avoiding unspecific nouns, and using uniform terminology are all recommended. Incomplete comparisons ("faster" without a reference) are a "thing to avoid."',
    chapter: 'EU 3',
  },
  // Q13 — A-type, 1pt
  {
    text: 'A template that provides a set of predefined fields to be filled in, for example when writing a use case, is called a:',
    options: [
      'Phrase template',
      'Form template',
      'Document template',
      'Specification pattern',
    ],
    answer: 1,
    points: 1,
    explanation: 'A form template provides predefined fields in a form (e.g., for a use case: actor, precondition, main flow, alternative flows). Phrase templates define syntactic structure for a sentence. Document templates structure a whole document.',
    chapter: 'EU 3',
  },
  // Q14 — K-type, 2pts
  {
    text: 'Which of the following statements about template-based work products are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Templates make requirements and requirements specifications look uniform.', answer: true },
      { text: 'Aspects not included in a template are more likely to be omitted.', answer: true },
      { text: 'Phrase templates, form templates, and document templates are the three types.', answer: true },
      { text: 'Templates eliminate the need for glossaries.', answer: false },
    ],
    points: 2,
    explanation: 'Templates provide uniformity but aspects outside the template may be missed. Three types exist. Templates do NOT replace glossaries — both serve different purposes (structure vs. terminology).',
    chapter: 'EU 3',
  },
  // Q15 — P-type, 2pts
  {
    text: 'Which TWO are rules for managing a glossary according to the syllabus? (Select two)',
    options: [
      'The glossary should be managed by each team independently',
      'The use of the glossary should be mandatory',
      'The glossary should only contain technical terms',
      'The glossary should be managed centrally',
      'Stakeholders should not be involved in glossary creation',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Glossary rules: manage centrally (not by each team independently), make usage mandatory, involve stakeholders (not exclude them). The glossary covers context-specific terms, everyday terms with special meaning, abbreviations, and acronyms — not just technical terms.',
    chapter: 'EU 3',
  },
  // Q16 — K-type, 2pts
  {
    text: 'Which of the following statements about models in RE are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Models reduce cognitive load by focusing on a single aspect of requirements.', answer: true },
      { text: 'When a non-standard modeling language is used, a legend explaining it is required.', answer: true },
      { text: 'Keeping models that focus on different aspects consistent is easy and straightforward.', answer: false },
      { text: 'Models and natural language are frequently combined in practice.', answer: true },
    ],
    points: 2,
    explanation: 'Models reduce cognitive load through focus. Non-standard languages need a legend. Keeping different-aspect models consistent is CHALLENGING (not easy). Models and natural language are frequently combined because each has limitations.',
    chapter: 'EU 3',
  },
  // Q17 — A-type, 1pt
  {
    text: 'In UML, what does a use case diagram primarily model?',
    options: [
      'The internal data structure of the system',
      'The system and its context in terms of use cases and actors that interact with the system',
      'The state transitions of system components',
      'The sequence of actions in a business process',
    ],
    answer: 1,
    points: 1,
    explanation: 'A UML use case diagram models a system and its context — showing the system\'s use cases and the actors in the system context that interact with the system through these use cases.',
    chapter: 'EU 3',
  },
  // Q18 — K-type, 2pts
  {
    text: 'Which of the following statements about UML class diagrams are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A multiplicity of "0..*" means zero or more instances can participate.', answer: true },
      { text: 'Generalization (inheritance) is shown with an arrow having a hollow triangle.', answer: true },
      { text: 'Composition means the part can exist independently of the whole.', answer: false },
      { text: 'Class diagrams can be used to model the static structure of a domain.', answer: true },
    ],
    points: 2,
    explanation: '0..* means zero or more. Generalization uses a hollow triangle arrow. In composition, the part CANNOT exist independently (that\'s aggregation). Class diagrams model static domain/system structure.',
    chapter: 'EU 3',
  },
  // Q19 — A-type, 1pt
  {
    text: 'Which UML diagram type is used to model state-dependent reactions to events?',
    options: [
      'Activity diagram',
      'Use case diagram',
      'Class diagram',
      'State machine diagram',
    ],
    answer: 3,
    points: 1,
    explanation: 'State machine diagrams model events that trigger transitions from one state to another and the actions performed during transitions. Activity diagrams model function/flow. Use case diagrams model context. Class diagrams model structure/data.',
    chapter: 'EU 3',
  },
  // Q20 — P-type, 2pts
  {
    text: 'Which TWO of the following are further model types mentioned at the Foundation Level (L1 — know only)? (Select two)',
    options: [
      'Goal models',
      'Deployment diagrams',
      'Domain story models',
      'Component diagrams',
      'Network topology diagrams',
    ],
    answer: [0, 2],
    multi: true,
    points: 2,
    explanation: 'The syllabus mentions goal models, domain story models, interaction models, and SysML block definition diagrams as further model types at L1. Deployment diagrams, component diagrams, and network topology diagrams are not listed.',
    chapter: 'EU 3',
  },
  // Q21 — K-type, 2pts
  {
    text: 'Which of the following statements about activity diagrams are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A join element synchronizes multiple concurrent flows back into one.', answer: true },
      { text: 'The initial node is represented by a filled circle.', answer: true },
      { text: 'Activity diagrams cannot express who is responsible for which action.', answer: false },
      { text: 'Activity diagrams can be used for both system functions and business processes.', answer: true },
    ],
    points: 2,
    explanation: 'Join synchronizes parallel flows. Initial node is a filled circle. Activity diagrams CAN express responsibility through swim lanes. They can model both system functions and business processes.',
    chapter: 'EU 3',
  },
  // Q22 — A-type, 1pt
  {
    text: 'Which type of exploratory prototype uses real screens and click flows but without real functionality?',
    options: [
      'Wireframe',
      'Mock-up',
      'Native prototype',
      'Evolutionary prototype',
    ],
    answer: 1,
    points: 1,
    explanation: 'Mock-ups are medium-fidelity: real screens, click flows, but no real functionality. Wireframes are low-fidelity (simple materials/sketches). Native prototypes are high-fidelity (implement critical parts). Evolutionary prototypes are pilot systems.',
    chapter: 'EU 3',
  },
  // Q23 — K-type, 2pts
  {
    text: 'Which of the following are quality criteria for single requirements and which are for multi-requirement work products?',
    type: 'ktype',
    statements: [
      { text: 'Adequate is a quality criterion for single requirements.', answer: true },
      { text: 'Consistent is a quality criterion for single requirements.', answer: false },
      { text: 'Modifiable is a quality criterion for work products containing multiple requirements.', answer: true },
      { text: 'Unambiguous is a quality criterion for single requirements.', answer: true },
    ],
    points: 2,
    explanation: 'Single requirement criteria: adequate, necessary, unambiguous, complete, understandable, verifiable. Multi-requirement work product criteria: consistent, non-redundant, complete, modifiable, traceable, conformant.',
    chapter: 'EU 3',
  },
  // Q24 — P-type, 2pts
  {
    text: 'Which TWO are frequently used alternative documentation structures (not classic documents)? (Select two)',
    options: [
      'System Requirements Specification',
      'Product backlog',
      'Vision Document',
      'Story map',
      'Business Requirements Specification',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Product backlog, sprint backlog, and story map are alternative documentation structures. System Requirements Specification, Vision Document, and Business Requirements Specification are classic documents.',
    chapter: 'EU 3',
  },
  // Q25 — A-type, 1pt
  {
    text: 'According to the syllabus, which two are the most important quality criteria for single requirements?',
    options: [
      'Verifiable and traceable',
      'Adequate and understandable',
      'Complete and consistent',
      'Necessary and unambiguous',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus states: "Adequacy and understandability are the most important quality criteria for single requirements. Without them, a requirement is useless or even harmful."',
    chapter: 'EU 3',
  },

  // ── EU 4: Practices for Elaboration (10 questions, 14 pts) ──
  // Q26 — A-type, 1pt
  {
    text: 'When should systematic stakeholder identification take place?',
    options: [
      'Only after the requirements specification is complete',
      'At the beginning of a development venture, managed as a continuous activity',
      'Only during the final validation phase',
      'Only when conflicts are identified',
    ],
    answer: 1,
    points: 1,
    explanation: 'Systematic identification should take place at the beginning and be managed throughout development as a continuous activity, including identifying both stakeholder roles and persons in those roles.',
    chapter: 'EU 4',
  },
  // Q27 — K-type, 2pts
  {
    text: 'Which of the following statements about the Kano model are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Satisfiers cause satisfaction proportional to their degree of fulfillment.', answer: true },
      { text: 'Dissatisfiers cause strong satisfaction when present.', answer: false },
      { text: 'Delighters are features that stakeholders do not expect but that cause strong satisfaction.', answer: true },
      { text: 'The Kano model classifies requirements into three relevant categories.', answer: true },
    ],
    points: 2,
    explanation: 'Satisfiers (performance factors) have proportional satisfaction. Dissatisfiers are taken for granted — their presence is NOT noticed (they don\'t cause satisfaction, only their absence causes dissatisfaction). Delighters are unexpected positives. Three categories: delighters, satisfiers, dissatisfiers.',
    chapter: 'EU 4',
  },
  // Q28 — A-type, 1pt
  {
    text: 'Which of the following is an example of a design and idea-generating technique?',
    options: [
      'Document analysis',
      'Structured interview',
      'Brainstorming',
      'Questionnaire',
    ],
    answer: 2,
    points: 1,
    explanation: 'Brainstorming is a design and idea-generating technique that stimulates creativity. Document analysis is artifact-based, interviews are questioning techniques, and questionnaires are questioning techniques — all are gathering techniques.',
    chapter: 'EU 4',
  },
  // Q29 — A-type, 1pt
  {
    text: 'A stakeholder list should include at least which information for each stakeholder?',
    options: [
      'Name and email only',
      'Name, role, availability, relevance, expertise, and goals/interests',
      'Name and the list of requirements they submitted',
      'Name, job title, and salary band',
    ],
    answer: 1,
    points: 1,
    explanation: 'The syllabus specifies: name, function (role), contact data, temporal/spatial availability, relevance, area and extent of expertise, and goals and interests regarding the project.',
    chapter: 'EU 4',
  },
  // Q30 — K-type, 2pts
  {
    text: 'Which of the following statements about conflict resolution are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'The four tasks are: conflict identification, conflict analysis, conflict resolution, and documentation.', answer: true },
      { text: 'Voting and overruling are both listed as conflict resolution techniques.', answer: true },
      { text: 'Ignoring a conflict is a recommended resolution strategy when the conflict is minor.', answer: false },
      { text: 'A "definition of variants" is a technique where multiple solution variants accommodate different needs.', answer: true },
    ],
    points: 2,
    explanation: 'Four tasks and the techniques (agreement, compromise, voting, overruling, definition of variants) are correct. Ignoring a conflict is NOT a listed resolution technique — conflicts should be actively resolved.',
    chapter: 'EU 4',
  },
  // Q31 — A-type, 1pt
  {
    text: 'Which of the following is NOT one of the four important aspects of requirements validation?',
    options: [
      'Involvement of the right stakeholders',
      'Separating identification and correction of defects',
      'Validation by the development team only',
      'Repeated validation',
    ],
    answer: 2,
    points: 1,
    explanation: 'The four aspects are: involving the right stakeholders, separating identification from correction, validation from DIFFERENT views (not just the dev team), and repeated validation.',
    chapter: 'EU 4',
  },
  // Q32 — K-type, 2pts
  {
    text: 'Which of the following statements about validation techniques are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Walkthroughs and inspections are review techniques.', answer: true },
      { text: 'Prototyping and A/B testing are exploratory validation techniques.', answer: true },
      { text: 'The choice of validation technique is independent of the development process.', answer: false },
      { text: 'Building a Minimum Viable Product (MVP) can be used as an exploratory validation technique.', answer: true },
    ],
    points: 2,
    explanation: 'Walkthroughs/inspections are review techniques; prototyping, A/B testing, and MVP are exploratory. The choice DEPENDS on the development process, complexity, risk level, etc.',
    chapter: 'EU 4',
  },
  // Q33 — A-type, 1pt
  {
    text: 'The best results in elicitation are usually achieved by:',
    options: [
      'Using only one proven technique throughout the project',
      'Focusing exclusively on interviewing key stakeholders',
      'A combination of different elicitation techniques',
      'Delegating elicitation entirely to the product owner',
    ],
    answer: 2,
    points: 1,
    explanation: 'The syllabus states: "The best results are usually achieved with a combination of different elicitation techniques." No single technique is sufficient.',
    chapter: 'EU 4',
  },
  // Q34 — A-type, 1pt
  {
    text: 'Which of the following correctly lists the six conflict types from the syllabus?',
    options: [
      'Technical, political, personal, financial, legal, organizational',
      'Subject matter, data, interest, value, relationship, structural',
      'Scope, schedule, budget, quality, resource, communication',
      'Requirement, design, code, test, deployment, maintenance',
    ],
    answer: 1,
    points: 1,
    explanation: 'The six types are: subject matter, data, interest, value, relationship, and structural conflict.',
    chapter: 'EU 4',
  },
  // Q35 — A-type, 1pt
  {
    text: 'What is the purpose of "personas" in requirements elicitation?',
    options: [
      'To replace stakeholder interviews entirely',
      'To represent end user groups when individuals cannot be identified',
      'To document the technical architecture of the system',
      'To prioritize requirements using the MoSCoW technique',
    ],
    answer: 1,
    points: 1,
    explanation: 'Personas are fictional archetypical descriptions defined as substitutes when end users cannot be individually identified or when there are too many individuals in a stakeholder role.',
    chapter: 'EU 4',
  },

  // ── EU 5: Process and Working Structure (2 questions, 3 pts) ──
  // Q36 — K-type, 2pts
  {
    text: 'Which of the following statements about RE process configurations are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'A participatory RE process is iterative, explorative, and customer-specific.', answer: true },
      { text: 'A contractual RE process uses a requirements specification as the contractual basis.', answer: true },
      { text: 'A product-oriented RE process is linear, prescriptive, and market-oriented.', answer: false },
      { text: 'The five-step configuration procedure starts with analyzing the influencing factors.', answer: true },
    ],
    points: 2,
    explanation: 'Participatory = iterative, explorative, customer-specific. Contractual = typically linear, prescriptive, customer-specific. Product-oriented = ITERATIVE, EXPLORATIVE, market-oriented (not linear/prescriptive). The five steps start with analyzing influencing factors.',
    chapter: 'EU 5',
  },
  // Q37 — A-type, 1pt
  {
    text: 'Which influencing factor determines that "no process can be chosen that builds upon continuous stakeholder feedback"?',
    options: [
      'High complexity of the system',
      'Stakeholders only available at the beginning of the project',
      'High volatility of requirements',
      'Limited experience of Requirements Engineers',
    ],
    answer: 1,
    points: 1,
    explanation: 'If stakeholders are only available at the beginning, no process relying on continuous feedback can be used. This is an example of how influencing factors constrain the space of possible process configurations.',
    chapter: 'EU 5',
  },

  // ── EU 6: Management Practices (6 questions, 10 pts) ──
  // Q38 — K-type, 2pts
  {
    text: 'Which of the following statements about requirements management are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Requirements management includes storing, changing, and tracing requirements.', answer: true },
      { text: 'Each documented requirement has its own life cycle with defined statuses and transitions.', answer: true },
      { text: 'A version number typically consists of at least two parts: the version and the increment.', answer: true },
      { text: 'Requirements management is only needed in large, regulated projects.', answer: false },
    ],
    points: 2,
    explanation: 'RM includes storing, changing, tracing. Each requirement has a life cycle. Version numbers have at least version + increment. RM is needed regardless of project size — the task is to maintain requirements so all roles can work effectively.',
    chapter: 'EU 6',
  },
  // Q39 — A-type, 1pt
  {
    text: 'What are the five properties of a requirements configuration?',
    options: [
      'Scope, schedule, budget, quality, and risk',
      'Logical connection, consistency, uniqueness, unchangeability, and basis for reset',
      'Completeness, correctness, consistency, traceability, and verifiability',
      'Identification, analysis, specification, validation, and management',
    ],
    answer: 1,
    points: 1,
    explanation: 'Configurations have five properties: logical connection, consistency, uniqueness, unchangeability, and basis for reset.',
    chapter: 'EU 6',
  },
  // Q40 — K-type, 2pts
  {
    text: 'Which of the following statements about attributes and views are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Attributes document important metadata for a work product.', answer: true },
      { text: 'A selective view filters requirements based on attribute values.', answer: true },
      { text: 'A projective view summarizes information across all requirements.', answer: false },
      { text: 'Views are typically combinations of selective, projective, and aggregating views for reports.', answer: true },
    ],
    points: 2,
    explanation: 'Attributes are metadata. Selective views filter by attributes. A PROJECTIVE view shows specific attributes (not summarizes — that is AGGREGATING). In practice, views combine all three types for reporting.',
    chapter: 'EU 6',
  },
  // Q41 — P-type, 2pts
  {
    text: 'Which TWO are common representation forms for explicit traceability? (Select two)',
    options: [
      'Verbal agreements in meetings',
      'Hyperlinks between work products',
      'Naming conventions in file structures',
      'Traceability matrices',
      'Oral presentations to stakeholders',
    ],
    answer: [1, 3],
    multi: true,
    points: 2,
    explanation: 'Common forms of EXPLICIT traceability include hyperlinks, references, matrices, tables, or graphs — all based on unique identifiers. Naming conventions and file structures are forms of IMPLICIT traceability. Verbal agreements and oral presentations are not traceability methods.',
    chapter: 'EU 6',
  },
  // Q42 — A-type, 1pt
  {
    text: 'In a linear (plan-driven) approach, who typically decides on a requirements change?',
    options: [
      'The product owner',
      'The development team',
      'A Change Control Board',
      'The individual Requirements Engineer',
    ],
    answer: 2,
    points: 1,
    explanation: 'In a linear approach, a Change Control Board (in projects) or Change Advisory Board (in operations) decides on changes. In agile, the product owner manages changes through the product backlog.',
    chapter: 'EU 6',
  },
  // Q43 — K-type, 2pts
  {
    text: 'Which of the following statements about prioritization are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'Assessment criteria for prioritization may include business value, urgency, effort, and dependencies.', answer: true },
      { text: 'Prioritization techniques are classified into ad-hoc and analytical techniques.', answer: true },
      { text: 'The steps for prioritization include selecting the technique before defining the requirements to prioritize.', answer: false },
      { text: 'The priority of a requirement describes its importance compared to other requirements.', answer: true },
    ],
    points: 2,
    explanation: 'Assessment criteria include business value, urgency, effort, dependencies. Ad-hoc and analytical are the two categories. The steps define requirements BEFORE selecting the technique (define requirements to prioritize → select technique → perform). Priority describes relative importance.',
    chapter: 'EU 6',
  },

  // ── EU 7: Tool Support (2 questions, 3 pts) ──
  // Q44 — K-type, 2pts
  {
    text: 'Which of the following statements about RE tools are true and which are false?',
    type: 'ktype',
    statements: [
      { text: 'RE tools can support management of requirements, management of the RE process, and documentation of knowledge.', answer: true },
      { text: 'Existing RE tools typically support all RE activities comprehensively.', answer: false },
      { text: 'When introducing tools, all life cycle costs beyond license costs should be considered.', answer: true },
      { text: 'General-purpose tools like spreadsheets are always sufficient for any project.', answer: false },
    ],
    points: 2,
    explanation: 'Three support categories are correct. Tools rarely support ALL activities. Life cycle costs beyond licenses must be considered. General-purpose tools have limitations — they should only be used when RE is in control and requirements are stable.',
    chapter: 'EU 7',
  },
  // Q45 — A-type, 1pt
  {
    text: 'The syllabus recommends using which approach to avoid risks when introducing an RE tool?',
    options: [
      'Immediately rolling out the tool to all teams',
      'Using pilot projects',
      'Letting each team choose their own tool independently',
      'Selecting the most expensive tool available',
    ],
    answer: 1,
    points: 1,
    explanation: 'Pilot projects are recommended to avoid risks when introducing RE tools. This allows testing the tool in a limited scope before a full rollout.',
    chapter: 'EU 7',
  },
]
</script>

# Sample Exam 2 (Syllabus v3.3.0)

::: info Official Practice Exam
The official IREB practice exam is free and available in 12 languages: [Download from IREB](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

<div class="exam-tip">
  <strong>Exam simulation:</strong> 45 questions, 70 points, 75-minute time limit, 70% passing score (49/70 pts). Covers all 7 Educational Units in the official format — single-select (A-type), pick-two (P-type), and true/false matrix (K-type) questions.
</div>

<ExamQuiz :questions="questions" />
