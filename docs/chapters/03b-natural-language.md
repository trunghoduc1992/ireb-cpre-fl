<script setup>
import Quiz from '../.vitepress/theme/Quiz.vue'

const questions = [
  {
    text: 'Which of the following is an advantage of natural-language-based work products?',
    options: [
      'They are always unambiguous',
      'They require specific training to read and understand',
      'They are extremely expressive and can express almost any requirement',
      'They automatically detect inconsistencies',
    ],
    answer: 2,
    explanation: 'Natural language is extremely expressive, flexible, and almost any requirement can be expressed in it. It requires no specific training to read. However, it is prone to ambiguity, and detecting inconsistencies in natural-language texts is difficult.',
  },
  {
    text: 'Which of the following is a "thing to avoid" (not just "use with care") when writing natural-language requirements?',
    options: [
      'Passive voice',
      'Nominalizations',
      'Incomplete descriptions',
      'Universal quantifiers',
    ],
    answer: 2,
    explanation: 'The syllabus distinguishes "things to avoid" (incomplete descriptions, unspecific nouns, incomplete conditions, incomplete comparisons) from "things to use with care" (passive voice, universal quantifiers, nominalizations).',
  },
  {
    text: 'What is the purpose of a glossary in Requirements Engineering?',
    options: [
      'To list all requirements in alphabetical order',
      'To record a central collection of term definitions that ensures shared understanding of terminology',
      'To provide a template for writing user stories',
      'To document the history of requirement changes',
    ],
    answer: 1,
    explanation: 'A glossary is a central collection of definitions for context-specific terms, everyday terms with special meaning, abbreviations, and acronyms. It mitigates the risk of different people interpreting the same terms differently.',
  },
  {
    text: 'Which THREE types of templates does the syllabus describe?',
    options: [
      'Phrase templates, form templates, and document templates',
      'User story templates, use case templates, and test case templates',
      'Code templates, design templates, and specification templates',
      'Simple templates, complex templates, and composite templates',
    ],
    answer: 0,
    explanation: 'The syllabus describes phrase templates (predefined syntactic structure for a requirement), form templates (predefined fields in a form, e.g., for use cases), and document templates (predefined structure for a whole document).',
  },
  {
    text: 'Which of the following is a disadvantage of template-based work products?',
    options: [
      'They make requirements look non-uniform',
      'They cannot capture the most relevant information',
      'People often focus on formal completion of the template rather than on content',
      'They reduce the overall quality of specifications',
    ],
    answer: 2,
    explanation: 'The syllabus lists two disadvantages: people focus on formal completion of templates rather than content, and aspects not included in the template are more likely to be omitted.',
  },
]
</script>

# EU 3: Natural Language and Template-Based Work Products

::: info Official Reference
**IREB CPRE-FL Syllabus v3.3.0** — Educational Unit 3, Sections 3.2, 3.3, 3.5 (L3)
[Download syllabus](https://cpre.ireb.org/en/downloads-and-resources/downloads)
:::

See also: [Work Product Basics](03a-work-product-basics) | [Model-Based Work Products](03c-models)

## 3.2 Natural-Language-Based Work Products (L2)

Since the inception of systematic RE, natural-language requirements have been a core means for specifying requirements in practice.

### Advantages

- Unconstrained natural language is **extremely expressive and flexible**
- Almost any conceivable requirement in any aspect can be expressed in natural language
- Natural language is used in everyday life and taught at school — **no specific training** is required to read and understand it

### Disadvantages

These advantages come at the expense that texts in natural language can frequently be **interpreted in different ways**, which is a problem when specifying requirements. Detection of ambiguities, omissions, and inconsistencies in such texts is **difficult and expensive**.

### Rules for Writing Good Natural-Language Requirements

Writing good requirements can be supported by:

- Writing **short and well-structured** sentences
- Defining and consistently using a **uniform terminology** (see Section 3.5 on glossaries)
- **Avoiding** vague or ambiguous terms and phrases
- Knowing the **pitfalls** of technical writing

### Pitfalls in Technical Writing

The syllabus distinguishes between things to **avoid** and things to **use with care**:

**Things to avoid:**

| Pitfall | Problem | Example |
|---------|---------|---------|
| Incomplete descriptions | Key information is missing | "The system shall process data." (What data? How?) |
| Unspecific nouns | Reader cannot determine what is being referred to | "The system shall store the information." (Which information?) |
| Incomplete conditions | Not all conditions are specified | "If the user is logged in, show the dashboard." (What if not logged in?) |
| Incomplete comparisons | Comparison lacks a reference point | "The system shall be faster." (Faster than what?) |

**Things to use with care:**

| Pitfall | Risk | Example |
|---------|------|---------|
| Passive voice | Hides the actor who performs the action | "The report shall be generated." (By whom?) |
| Universal quantifiers | "All" or "never" may over-promise | "The system shall never crash." |
| Nominalizations | Nouns derived from verbs hide actor and action | "The authentication shall take place." → "The system shall authenticate the user." |

## 3.3 Template-Based Work Products (L3)

Template-based work products overcome some shortcomings of natural language by providing **predefined structures** for requirements.

### Types of Templates

| Template Type | Purpose | Example |
|---------------|---------|---------|
| **Phrase templates** | Predefined syntactic structure for a single requirement or user story | "The \<system\> shall \<action\> \<object\> \<condition\>." |
| **Form templates** | Predefined fields in a form | Use case template with fields for actor, precondition, main flow, alternative flows |
| **Document templates** | Predefined structure for a whole document | ISO/IEC/IEEE 29148 specification template |

<div class="example-box">

**Phrase template for an individual requirement:**
"The system shall \<verb\> \<object\> \<condition\>."

**Example:** "The system **shall calculate** the total order amount **including applicable taxes** when the user proceeds to checkout."

**Phrase template for a user story:**
"As a \<role\>, I want \<goal\>, so that \<benefit\>."

**Example:** "As a **customer**, I want **to filter products by price range**, so that **I can quickly find items within my budget**."

</div>

### Advantages

- Provide a clear, re-usable structure
- Help to capture the most relevant information
- Make requirements look uniform
- Improve the overall quality of requirements and specifications

### Disadvantages

- People often focus on **formal completion** of the template rather than on content
- Aspects **not included** in the template are more likely to be omitted

## 3.5 Glossaries (L2)

In every RE endeavor involving more than one person, there is a risk that people interpret the same terms in different ways. A **glossary** mitigates this problem.

<div class="key-concept">

A **glossary** is a central collection of definitions for: context-specific terms, everyday terms with a special meaning in the given context, abbreviations, and acronyms.

</div>

**Synonyms** (different terms for the same thing) should be marked. **Homonyms** (same term for different things) should be avoided or marked.

### Glossary Rules

1. Manage the glossary **centrally**
2. Maintain the glossary over the **entire course** of system development
3. Define a **responsible person** or small group for the glossary
4. Use a **uniform style and structure**
5. **Involve stakeholders** and seek agreement about the terminology
6. Make the glossary **accessible** for everybody involved
7. Make the use of the glossary **mandatory**
8. **Check** work products for proper glossary usage

## Practice Quiz

<Quiz :questions="questions" />
