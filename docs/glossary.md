<script setup>
import { ref, computed } from 'vue'

const searchTerm = ref('')

const terms = [
  { term: 'Acceptance Criteria', definition: 'Conditions that a system must satisfy to be accepted by a stakeholder. Used to verify that a requirement has been fulfilled.' },
  { term: 'Activity Diagram', definition: 'A UML diagram that models the flow of activities in a process, including decisions, parallel execution (fork/join), and swim lanes.' },
  { term: 'Actor', definition: 'A person or external system that interacts with the system under development. Represented as a stick figure in use case diagrams.' },
  { term: 'Aggregation', definition: 'A "has-a" relationship in class diagrams where the part can exist independently of the whole. Shown as a hollow diamond.' },
  { term: 'Ambiguity', definition: 'A quality defect where a requirement can be interpreted in more than one way.' },
  { term: 'Baseline', definition: 'A formally agreed-upon and frozen snapshot of requirements at a specific point in time. Changes after baselining must go through change control.' },
  { term: 'Brainstorming', definition: 'A creative group elicitation technique for generating many ideas quickly, with rules: no criticism, quantity over quality, build on others\' ideas.' },
  { term: 'Change Control Board (CCB)', definition: 'A group authorized to evaluate, approve, or reject change requests to baselined requirements.' },
  { term: 'Change Request', definition: 'A formal proposal to modify a baselined requirement. Must include impact analysis before approval.' },
  { term: 'Class Diagram', definition: 'A UML diagram showing the data structure of a domain: classes (entities), their attributes, and relationships (associations, generalizations, aggregations, compositions).' },
  { term: 'Composition', definition: 'A strong "has-a" relationship in class diagrams where the part cannot exist without the whole. Shown as a filled diamond.' },
  { term: 'Conflict', definition: 'A situation where two or more requirements contradict each other, or stakeholders have incompatible expectations.' },
  { term: 'Constraint', definition: 'A requirement that restricts the solution space. Imposed by organizational, technological, legal, or physical factors. Typically non-negotiable.' },
  { term: 'Context Boundary', definition: 'The boundary separating the relevant system context from the irrelevant environment.' },
  { term: 'Context Diagram', definition: 'A high-level diagram showing the system under development, its boundary, external entities (users, systems), and the interactions between them.' },
  { term: 'Document Analysis', definition: 'An elicitation technique that studies existing documentation (forms, reports, manuals) to extract requirements. Also called "archaeology."' },
  { term: 'Elicitation', definition: 'The RE activity of discovering, gathering, and developing requirements from stakeholders and other sources.' },
  { term: 'Entity-Relationship Diagram', definition: 'A data modeling diagram showing entities, their attributes, and relationships with cardinalities. Similar purpose to class diagrams.' },
  { term: 'Extend (Use Case)', definition: 'A relationship where an extending use case optionally adds behavior to a base use case under certain conditions. Arrow points from extending to base use case.' },
  { term: 'Feasibility', definition: 'A quality criterion: the requirement can realistically be implemented within the given constraints (technical, budget, time).' },
  { term: 'Fork', definition: 'An element in activity diagrams (thick bar) that splits a single flow into multiple concurrent (parallel) flows.' },
  { term: 'Functional Requirement', definition: 'A requirement describing what the system does — a function, behavior, or data it must provide.' },
  { term: 'Generalization (Actor)', definition: 'In use case diagrams, an actor that inherits all use cases of a more general actor (e.g., Admin inherits from User).' },
  { term: 'Generalization (Class)', definition: 'In class diagrams, inheritance — a subclass inherits attributes and operations from a superclass.' },
  { term: 'Glossary', definition: 'A collection of agreed-upon term definitions used in a project to avoid ambiguity and ensure shared understanding among stakeholders.' },
  { term: 'Goal Model', definition: 'A model showing stakeholder goals and their decomposition into sub-goals, eventually leading to concrete requirements.' },
  { term: 'Guard Condition', definition: 'A boolean condition (in square brackets) on a state machine transition that must be true for the transition to occur.' },
  { term: 'Impact Analysis', definition: 'The process of determining what artifacts (requirements, design, code, tests) are affected by a proposed change. Enabled by traceability.' },
  { term: 'Include (Use Case)', definition: 'A relationship where a base use case always incorporates the behavior of the included use case. The included behavior is mandatory.' },
  { term: 'Inspection', definition: 'The most formal review technique with defined roles (moderator, author, reviewers, scribe), mandatory preparation, and a structured process for defect detection.' },
  { term: 'Interview', definition: 'An elicitation technique: a structured or semi-structured conversation with a stakeholder to explore their needs and perspectives in depth.' },
  { term: 'Join', definition: 'An element in activity diagrams (thick bar) that synchronizes multiple concurrent flows back into a single flow.' },
  { term: 'Kano Classification', definition: 'A prioritization technique classifying requirements by customer satisfaction impact: basic (expected), performance (proportional), excitement (delighter).' },
  { term: 'MoSCoW', definition: 'A prioritization technique categorizing requirements as Must have, Should have, Could have, or Won\'t have (this time).' },
  { term: 'Model', definition: 'An abstract representation of a system or domain aspect using a defined notation. Used to reduce ambiguity and provide specific perspectives.' },
  { term: 'Multiplicity', definition: 'In class/ER diagrams, the number of instances that can participate in a relationship. Notations: 1, 0..1, 0..*, 1..*, etc.' },
  { term: 'Natural Language', definition: 'Requirements written in everyday human language. Universally readable but prone to ambiguity.' },
  { term: 'Negotiation', definition: 'The process of resolving conflicts between stakeholders with incompatible requirements or expectations.' },
  { term: 'Nominalization', definition: 'A language defect in requirements where verbs are turned into nouns, hiding the actor and action (e.g., "the calculation" instead of "the system calculates").' },
  { term: 'Observation', definition: 'An elicitation technique where the RE watches stakeholders perform their actual work to discover tacit knowledge and real workflows.' },
  { term: 'Pairwise Comparison', definition: 'A prioritization technique that systematically compares every requirement against every other to produce a relative ranking.' },
  { term: 'Perspective-Based Reading', definition: 'A review/elicitation technique where documents are examined from specific stakeholder perspectives (user, developer, tester) to find different types of issues.' },
  { term: 'Post-Requirements Traceability', definition: 'Links from requirements forward to downstream artifacts: design, code, and test cases.' },
  { term: 'Pre-Requirements Traceability', definition: 'Links from requirements backward to their sources: stakeholders, regulations, business goals.' },
  { term: 'Prioritization', definition: 'The process of determining the relative importance of requirements to guide implementation order and scope decisions.' },
  { term: 'Prototyping', definition: 'Creating a preliminary model of the system (throwaway or evolutionary) to help stakeholders understand and refine requirements.' },
  { term: 'Quality Requirement', definition: 'A requirement specifying how well the system performs its functions: performance, usability, reliability, security, maintainability, portability. Also called non-functional requirement.' },
  { term: 'Questionnaire', definition: 'An elicitation technique using written questions distributed to many stakeholders. Scalable but lacks interactive follow-up.' },
  { term: 'Requirement', definition: 'A condition or capability needed by a stakeholder to solve a problem or achieve an objective, that must be met or possessed by a system or system component.' },
  { term: 'Requirements Attribute', definition: 'Metadata attached to a requirement: ID, priority, status, source, author, version, risk, stability, etc.' },
  { term: 'Requirements Engineer', definition: 'The person responsible for eliciting, documenting, validating, and managing requirements. Acts as a mediator between stakeholders and the development team.' },
  { term: 'Requirements Engineering', definition: 'The systematic approach to eliciting, documenting, validating, and managing requirements throughout a project.' },
  { term: 'Requirements Management', definition: 'The RE activity of organizing, tracking, and controlling requirements: attributes, prioritization, traceability, versioning, and change management.' },
  { term: 'Requirements Specification', definition: 'A document describing WHAT the system must do from the stakeholder perspective (problem-oriented). Contrast with System Specification.' },
  { term: 'Sentence Template', definition: 'A standardized syntactic pattern for writing requirements (e.g., "The <system> shall <verb> <object> <condition>") to ensure consistency and reduce ambiguity.' },
  { term: 'Shall / Should / May', definition: 'Obligation keywords: "shall" = mandatory, "should" = recommended, "may"/"can" = optional. Based on RFC 2119 conventions.' },
  { term: 'Stakeholder', definition: 'A person or organization that has a direct or indirect influence on the system\'s requirements, or is affected by the system.' },
  { term: 'State Machine Diagram', definition: 'A UML diagram showing the states an entity can be in, the transitions between states, and the events/guards/actions that trigger transitions.' },
  { term: 'System Boundary', definition: 'The boundary separating the system under development from its environment (the system context).' },
  { term: 'System Context', definition: 'The part of the environment that is relevant to defining the system\'s requirements: interacting users, external systems, processes, regulations.' },
  { term: 'System Specification', definition: 'A document describing HOW the system will behave from the developer perspective (solution-oriented). Contrast with Requirements Specification.' },
  { term: 'System under Development (SuD)', definition: 'The system currently being specified and built. The focus of the RE effort.' },
  { term: 'Traceability', definition: 'The ability to follow a requirement from its origin (source), through its specification, to its implementation and verification in downstream artifacts.' },
  { term: 'Traceability Matrix', definition: 'A table linking requirements to their sources, design elements, code modules, and test cases.' },
  { term: 'Use Case', definition: 'A description of a specific interaction between an actor and the system to achieve a goal. Includes main flow, alternative flows, and exception flows.' },
  { term: 'Use Case Diagram', definition: 'A UML diagram showing actors, use cases, the system boundary, and relationships (association, include, extend, generalization).' },
  { term: 'Validation', definition: 'Checking that requirements correctly reflect stakeholder intentions and meet quality criteria. "Are we building the right thing?"' },
  { term: 'Verification', definition: 'Checking that an artifact conforms to its specification. "Are we building the thing right?"' },
  { term: 'Versioning', definition: 'Tracking changes to requirements by assigning version numbers and maintaining a change history.' },
  { term: 'Walkthrough', definition: 'A review technique where the author leads reviewers through a document, explaining its content. Low to medium formality.' },
  { term: 'Workshop', definition: 'A facilitated group session with multiple stakeholders to collaboratively define, discuss, and prioritize requirements.' },
]

const filteredTerms = computed(() => {
  if (!searchTerm.value) return terms
  const q = searchTerm.value.toLowerCase()
  return terms.filter(
    t => t.term.toLowerCase().includes(q) || t.definition.toLowerCase().includes(q)
  )
})
</script>

# Glossary

A searchable reference of all key IREB CPRE-FL terms and definitions.

<div style="margin: 1.5rem 0;">
  <input
    v-model="searchTerm"
    type="text"
    placeholder="Search terms..."
    style="
      width: 100%;
      padding: 0.6rem 1rem;
      border: 1px solid var(--vp-c-divider);
      border-radius: 8px;
      background: var(--vp-c-bg);
      color: var(--vp-c-text-1);
      font-size: 1rem;
      outline: none;
    "
  />
</div>

<div v-if="filteredTerms.length === 0" style="color: var(--vp-c-text-2); padding: 1rem;">
  No terms match your search.
</div>

<div v-for="t in filteredTerms" :key="t.term" style="margin-bottom: 1rem; padding: 0.75rem 1rem; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: var(--vp-c-bg-soft);">
  <strong>{{ t.term }}</strong>
  <p style="margin: 0.25rem 0 0 0; color: var(--vp-c-text-2); font-size: 0.95em;">{{ t.definition }}</p>
</div>
