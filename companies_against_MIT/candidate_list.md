# MIT-licensed Code, Attribution, and Corporate Avoidance Policies

## 1. Executive summary

- No public, citable evidence was found that any large, market‑influential company explicitly avoids or bans MIT‑licensed code because of the MIT license’s attribution requirement in binaries or other user‑facing products.  
- In contrast, major vendors such as Microsoft, Google, Meta, Apple, and Amazon widely use MIT‑licensed components and often release key projects under MIT, while managing attribution through standard notice mechanisms.[1][6][7][8][9][10][11][12][13][14][15][16]  
- Industry guidance from OSPOs, open‑source foundations, and compliance vendors consistently treats MIT as a low‑risk, standard permissive license. Avoidance policies are instead focused on copyleft licenses and patent issues.[17][18][19][21][22][23][24][25]

The overall weight of evidence indicates that MIT‑attribution‑driven avoidance is either extremely rare or, at least, not documented in public policies of major companies.

---

## 2. MIT license and attribution obligations

- The canonical MIT license requires that the copyright notice and permission notice be included in all copies or substantial portions of the software, including redistributed binaries.[1][2]  
- The license does not require source‑code disclosure, copyleft propagation, or an explicit patent grant.[1][2]

- Other common permissive licenses, such as BSD and Apache‑2.0, also require preservation of copyright and license notices. Apache‑2.0 additionally uses a NOTICE file mechanism for attribution.[1][2]  
- Since Apache‑2.0 and BSD are widely adopted by enterprises, their similar or greater notice requirements suggest that attribution alone is not viewed as a decisive barrier.

---

## 3. Search scope and methodology (high level)

The research focused on finding documents that simultaneously:

1. Name the MIT license specifically.  
2. State that MIT‑licensed components are avoided, forbidden, or discouraged in products or codebases.  
3. Attribute this stance to MIT’s attribution or notice‑preservation requirements in binaries or user‑facing contexts.

Materials examined included:

- Public open‑source policies and OSPO documentation from major vendors such as Microsoft, Google, Meta, Apple, and Amazon.[6][11][12][14][15][16]  
- Licenses and third‑party notice files for flagship projects and products that show real‑world inbound MIT usage.[7][8][9][10][13][14][20]  
- OSPO playbooks and governance guidance from Johns Hopkins, Georgia Tech, GitHub, and the TODO Group.[17][18][19][21]  
- Compliance and legal analyses from Snyk, FOSSA, Black Duck, the Linux Foundation, and OpenChain.[21][22][23][24][25]

No document was found that meets all three criteria.

---

## 4. Confirmed positive cases

### 4.1 Outcome

- No confirmed positive cases were identified.  
- For no large, market‑influential company was there any public policy, guideline, or authoritative statement that:

  - Names the MIT license,  
  - Explicitly forbids or discourages using MIT‑licensed components, and  
  - Explicitly cites MIT’s attribution or notice‑preservation requirement in binaries or user‑facing products as the reason.

### 4.2 Why the absence is meaningful

- Where companies publish explicit disallowed‑license lists or restrictions, these lists typically focus on AGPL, SSPL, some GPL contexts, and occasionally other niche licenses.[16][23][24][25]  
- The same documents treat MIT as a standard permissive or notice‑based license, often recommended or preferred, which strongly suggests that attribution obligations under MIT are not viewed as a primary risk factor.

---

## 5. Plausible but inconclusive signals

### 5.1 MIT‑0 (MIT No Attribution)

- MIT‑0 is an OSI‑approved variant of MIT that removes the requirement to preserve copyright and license notices, while retaining a broad grant of rights.[4]  
- AWS maintains a public MIT‑0 template and explains that it is useful when code is intended as reference, teaching samples, or templates that others may copy into their own products, where even minor attribution friction is undesirable.[4][5]

- This clearly shows that some publishers want to relieve downstream users of attribution duties, especially for snippet‑like code.  
- However, these materials describe outbound licensing choices and do not state that AWS or other large vendors avoid inbound MIT‑licensed dependencies for attribution reasons.[4][5][12][13]

### 5.2 Boost Software License

- The Boost Software License 1.0 is a permissive license that requires notices to be included in copies and derivative works, except when the software is distributed solely as compiled object code.[3]  
- This object‑code carve‑out changes how attribution requirements apply when distributing only compiled object code under this license.[3]

- This demonstrates that binary‑level attribution is recognized as an operational cost in some communities.  
- It remains a design choice at license level; no public corporate policy was found that instructs engineers to favor Boost over MIT for inbound code specifically to avoid attribution.

### 5.3 Individual or small‑vendor preferences

- Various blog posts and legal commentaries recommend MIT‑0 or similar licenses for authors who wish to publish code without imposing attribution on downstream users.[4][5]  
- These sources are about license selection by authors, not about inbound license policies of large enterprises.

---

## 6. Negative findings for major companies

The table below summarizes evidence for key vendors.

| Company | Evidence of MIT usage | Any MIT‑specific avoidance due to attribution? | Key indicators |
|--------|------------------------|-----------------------------------------------|----------------|
| Microsoft | Operates a large open‑source portal.[6] Releases Visual Studio Code, TypeScript, and the .NET runtime under MIT.[7][8][9] Publishes extensive third‑party notices for products that include MIT components.[14] | None found. Public practice and licensing show MIT as first‑class; compliance guidance focuses on copyleft and patents, not avoiding MIT notices. | MIT licensing of flagship developer tools and presence of MIT in third‑party notices. |
| Google | Runs a substantial open‑source program with detailed third‑party licensing guidance.[15][16] Public materials classify licenses and explicitly restrict AGPL, OSL, and SSPL, while not listing MIT as disallowed.[16] | None found. MIT appears as a standard permissive or notice‑based license; restrictions are aimed at strong copyleft and unusual licenses instead. | Explicit disallow lists that omit MIT, plus broad MIT usage in the ecosystem. |
| Meta (Facebook) | React and related projects are licensed under MIT.[10] Meta publicly relicensed React, Jest, Flow, and Immutable.js from a custom BSD‑plus‑patent license to MIT to reduce friction for adopters.[11] | None found. The relicensing rationale is about community comfort and patent concerns, not attribution; Meta’s own flagship projects actively use MIT. | MIT relicensing statement and ongoing MIT use. |
| Apple | Provides an open‑source portal listing Apple and third‑party components, including many under MIT, for macOS, iOS, and other products.[11] | None found. Apple ships MIT‑licensed components and fulfills attribution through standard acknowledgments and license bundles. | Public distribution of source and notices for MIT components. |
| Amazon / AWS | Operates an open‑source portal showing projects under MIT and Apache‑2.0.[12] Uses MIT‑licensed dependencies in services such as Amazon Pay, documented via an open‑source attributions page.[13] Also publishes MIT‑0 for some outbound code.[4][5] | None found. Evidence shows extensive inbound and outbound MIT use; MIT‑0 is an additional outbound option, not a signal of inbound avoidance. | Attributions listing MIT components and active promotion of MIT‑family licenses. |
| GitHub | OSPO releasing policy explicitly lists MIT as the preferred outbound license, with other licenses requiring legal review.[19] | None found. MIT is favored rather than avoided, indicating a view of MIT as simple and safe. | Direct policy language preferring MIT. |
| Academic and institutional OSPOs (JHU, Georgia Tech) | Johns Hopkins OSPO lists MIT, BSD‑3‑Clause, and Apache‑2.0 as the most commonly used permissive licenses.[17] Georgia Tech OSPO lists MIT, BSD, Apache‑2.0, and LGPL as preferred, and flags GPLv3 and AGPL as not preferred.[18] | None found. These guides strongly endorse MIT as a standard permissive choice. | Explicit preference lists that include MIT. |

Across these organizations, the pattern is consistent:

- MIT is used widely for both inbound dependencies and outbound open‑source projects.  
- Attribution obligations are handled via consolidated notice files, LICENSE bundles, and product‑specific acknowledgments, not by avoiding MIT.

---

## 7. Industry governance and legal perspectives

### 7.1 OSPO and foundation guidance

- The TODO Group’s OSPO guides, Johns Hopkins OSPO, Georgia Tech OSPO, and GitHub’s OSPO all treat MIT as a standard permissive license and often place it in the preferred or commonly used category.[17][18][19][21]  
- These materials emphasize building license inventories, approval workflows, and automated notice‑file generation, rather than avoiding licenses with notice obligations.

- None of these governance documents single out MIT’s attribution requirement in binaries as problematic.  
- Instead, they identify copyleft and network‑copyleft licenses as the most challenging for commercial use.

### 7.2 Compliance and attribution practice

- AboutCode’s best‑practices guide for open‑source attribution documents how large products aggregate license notices and attributions into credits pages, text files, or documentation bundles.[20]  
- The Linux Foundation’s compliance terminology and OpenChain training describe attribution and license‑notice obligations as routine compliance tasks that apply to many permissive licenses, including MIT.[21][22]

- The overall message is that attribution should be managed through process and tooling, not by avoiding permissive licenses.  
- This supports the observation that companies invest in attribution workflows instead of banning MIT.

### 7.3 Legal and risk assessments

- Snyk’s guide describes MIT as one of the simplest and most business‑friendly open‑source licenses, with primary obligations to preserve copyright and license text.[23]  
- FOSSA’s MIT overview characterizes it as an extremely popular permissive license with very few restrictions, contrasting it with GPL and AGPL.[24]

- Black Duck’s survey of top open‑source licenses finds that MIT is among the most widely used licenses in modern codebases and on GitHub.[25]  
- None of these analyses recommend avoiding MIT because of attribution requirements; instead, they recommend inventory and notice‑generation practices to ensure compliance.

---

## 8. Distinguishing MIT from other licensing concerns

### 8.1 Copyleft and source‑disclosure obligations

- Many large companies restrict or avoid AGPL, some GPLv3 uses, and similar licenses because they can trigger obligations to provide source code, installation information, or extended network‑use rights.[16][23][24][25]  
- MIT does not impose any such source‑disclosure or reciprocity obligations.[1][2][23][24]

- Public disallow lists and internal policy summaries usually name these copyleft licenses explicitly.  
- MIT is not grouped with them, which strongly suggests that MIT is not being avoided for similar reasons.

### 8.2 Patent and indemnity issues

- Enterprises often favor Apache‑2.0 over bare MIT for outbound code because Apache‑2.0 includes an explicit patent grant and termination clause, whereas MIT is silent on patents.[1][23][24]  
- This preference is about patent risk management for code the company publishes.

- The same companies still consume MIT‑licensed dependencies extensively, which shows that any Apache preference does not translate into inbound avoidance of MIT.  
- If attribution were the decisive factor, Apache‑2.0’s NOTICE requirements and BSD attribution terms would raise similar concerns, yet they are widely accepted.

### 8.3 Attribution as a manageable cost

- Attribution requirements under MIT, BSD, and Apache‑2.0 are widely treated as a relatively low, but real, compliance cost that can be addressed through automation and standardized processes.[20][21][22][23][24]  
- MIT‑0 and Boost demonstrate that some authors go further and remove or narrow attribution duties for the benefit of downstream users.[3][4][5]

- There is still no evidence that major companies respond to these costs by banning inbound MIT.  
- Instead, they respond by building better software composition analysis, bill‑of‑materials generation, and notice‑assembly tooling.

---

## 9. Overall assessment and implications

### 9.1 Summary of findings

The table below maps the core elements of the research brief to the evidence found.

| Research question element | Evidence pattern | Assessment |
|---------------------------|------------------|-----------|
| Do large companies explicitly avoid MIT because of attribution in binaries or user‑facing products? | No such explicit policies or statements were found for major vendors, despite extensive searching of OSPO documents, legal FAQs, and engineering blogs. | These MIT‑attribution‑driven avoidance policies appear to be rare to nonexistent in public documentation. |
| How do large companies actually treat MIT? | MIT is used extensively for inbound dependencies and outbound flagship projects (for example, VS Code, TypeScript, .NET, React) and is often categorized as a preferred or standard permissive license.[6][7][8][9][10][11][17][18][19] | MIT is treated as a low‑risk, mainstream choice. |
| Are there MIT‑like licenses designed to reduce attribution cost? | MIT‑0 removes attribution entirely; Boost removes notice obligations for pure object‑code distribution.[3][4][5] | These show that attribution is a recognized cost, but not that MIT is avoided as a result. |
| How do governance bodies and legal guides view MIT? | OSPO playbooks, Linux Foundation and OpenChain materials, and legal vendors characterize MIT as simple and widely adopted, focusing concern on copyleft and patent‑heavy licenses instead.[17][18][19][21][22][23][24][25] | Industry guidance does not flag MIT attribution as a major adoption risk. |

### 9.2 Implications for license choice

- Organizations choosing a license for new projects should not assume that MIT’s attribution requirement alone will materially deter adoption by large enterprises.  
- Existing practice shows that major vendors already consume and ship substantial volumes of MIT‑licensed code and have built mature processes to handle attribution.[6][7][8][9][10][11][12][13][14][15][16]

- Licenses like MIT‑0 or Boost may still be attractive when the goal is to minimize any attribution friction for downstream users, particularly for embedded snippets, configuration templates, or space‑constrained UIs.[3][4][5]  
- However, the publicly available record does not support framing MIT’s attribution clause as a common or documented reason for avoidance by large, market‑influential companies.

---

### Sources

[1] MIT License – Open Source Initiative: https://opensource.org/license/mit  
[2] MIT License – Wikipedia: https://en.wikipedia.org/wiki/MIT_License  
[3] Boost Software License 1.0 – Open Source Initiative: https://opensource.org/license/bsl-1-0  
[4] MIT No Attribution License – Open Source Initiative: https://opensource.org/license/mit-0  
[5] MIT No Attribution (MIT‑0) – AWS GitHub: https://github.com/aws/mit-0  
[6] Microsoft Open Source: https://opensource.microsoft.com  
[7] Visual Studio Code License (MIT) – GitHub: https://github.com/microsoft/vscode/blob/main/LICENSE.txt  
[8] TypeScript License (MIT) – GitHub: https://github.com/microsoft/TypeScript/blob/main/LICENSE.txt  
[9] .NET Runtime License (MIT) – GitHub: https://github.com/dotnet/runtime/blob/main/LICENSE.TXT  
[10] React License (MIT) – GitHub: https://github.com/facebook/react/blob/main/LICENSE  
[11] Relicensing React, Jest, Flow, and Immutable.js – Meta Engineering: https://engineering.fb.com/2017/09/22/web/relicensing-react-jest-flow-and-immutable-js  
[12] AWS Open Source: https://aws.amazon.com/opensource  
[13] Amazon Pay – Open Source Attributions: https://developer.amazon.com/docs/amazon-pay-checkout/open-source-attributions.html  
[14] Microsoft Third‑Party Notices: https://www.microsoft.com/en-us/legal/third-party-notices  
[15] Google Open Source: https://opensource.google  
[16] Google – Third‑Party Licenses Guidance: https://opensource.google/documentation/reference/thirdparty/licenses  
[17] Johns Hopkins OSPO – Open Source Software and Licenses: https://ospo.library.jhu.edu/open-source-software-and-licenses  
[18] Georgia Tech OSPO – Open Source Software Licensing: https://ospo.cc.gatech.edu/open-source-software-licensing  
[19] GitHub OSPO – Releasing Policy: https://github.com/github/github-ospo/blob/main/policies/releasing.md  
[20] AboutCode – Best Practices for OSS Attribution: https://aboutcode.org/2015/oss-attribution-best-practices  
[21] Linux Foundation – Compliance Terminology for Developers: https://compliance.linuxfoundation.org/developers/terminology  
[22] OpenChain Curriculum Release 2 (PDF): https://wiki.linuxfoundation.org/_media/openchain/openchain-curriculum-release-2-with-notes.pdf  
[23] Snyk – What is the MIT License: https://snyk.io/learn/what-is-mit-license  
[24] FOSSA – Open Source Licenses 101: The MIT License: https://fossa.com/blog/open-source-licenses-101-mit-license  
[25] Black Duck – Top Open Source Licenses: https://www.blackduck.com/blog/top-open-source-licenses.html