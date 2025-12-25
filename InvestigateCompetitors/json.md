# Competitor Analysis: JSON

**Generated:** 2025-12-26T05:12:38.375255

**Library Info:**
- **Name:** JSON
- **C++ Version:** C++11
- **Description:**   JSON parsing, serialization, and DOM in C++11
- **URL:** https://www.boost.org/library/1.90.0/json/

---

## Usage Statistics

- **Input tokens:** 216,555
- **Output tokens:** 90,373
- **Total tokens:** 306,928
- **Tavily calls:** 7

---

## Pricing Information

### Summarization Model Costs

**Model:** openai/gpt-5-nano
- **Input tokens:** 22,671
- **Output tokens:** 20,577
- **Input cost:** $0.00 ($0.10 per 1K tokens)
- **Output cost:** $0.01 ($0.40 per 1K tokens)
- **Summarization model total:** $0.01

### Writer Model Costs

**Model:** openai/gpt-5.1
- **Input tokens:** 133,604
- **Output tokens:** 55,132
- **Input cost:** $0.33 ($2.50 per 1K tokens)
- **Output cost:** $0.55 ($10.00 per 1K tokens)
- **Writer model total:** $0.89

### Evaluator Model Costs (Red Team)

**Model:** google/gemini-2.5-flash
- **Input tokens:** 60,280
- **Output tokens:** 14,664
- **Input cost:** $0.00 ($0.07 per 1K tokens)
- **Output cost:** $0.00 ($0.30 per 1K tokens)
- **Evaluator model total:** $0.01

### Tavily API Costs

- **API calls:** 7
- **Cost per call:** $0.008
- **Tavily total:** $0.06

### Total Cost

**Total LLM cost:** $0.90
**Estimated total cost:** $0.96

---
# Quantitative comparison of Boost.JSON and competing C++ JSON libraries (re‑refined, further objectivity‑checked)

All quantitative data are approximate as of 2024‑10, based on public GitHub statistics, project documentation, package managers, and neutral benchmarks. Where only qualitative judgments are possible, they are labeled as such, and limitations are noted.

## 1 Scope and libraries

Focus: C++11+ JSON libraries with DOM parsing and serialization, compared to Boost.JSON, using GitHub and benchmark data where possible.

### 1.1 Libraries overview

For competitors, advantages and disadvantages are vs Boost.JSON. For the Boost.JSON row, they are vs this set of competitors overall.

| Library       | GitHub URL                          | Short description                                                                 | Main advantage vs peers                                                                                                      | Main disadvantage vs peers                                                                                                                                                       | Stars approx* | Last notable release (tag)                            | Min C++ |
|--------------|--------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|--------------------------------------------------------|--------:|
| Boost.JSON   | https://github.com/boostorg/json    | Boost library for DOM and streaming JSON with allocator control and Boost stack integration [1][2]. | Tight integration with Boost (Beast, Asio), error codes, and allocator customization that fits existing Boost/pmr usage [1][2]. | Requires Boost as a dependency and has far fewer GitHub stars and direct dependents than nlohmann/json, suggesting lower visible standalone reuse on GitHub; however, Boost‑internal reuse is not fully captured by these metrics [1][2][3][15]. |        ~0.5k | Part of current Boost 1.8x releases as of 2024‑10 [1]. |      11 |
| nlohmann/json | https://github.com/nlohmann/json   | Header‑only JSON for Modern C++ with STL‑like API and implicit conversions [3][4]. | Very expressive, idiomatic C++ API and by far the highest GitHub star and dependent counts in this set [3][4][15].          | Generally slower at run time than RapidJSON and simdjson and with high compile‑time cost; RapidJSON and Boost.JSON often build faster in published benchmarks [7][12].            |        ~48k  | v3.11.3 (2023‑09) [3].                                 |      11 |
| RapidJSON    | https://github.com/Tencent/rapidjson | High‑performance DOM and SAX library focused on low latency and memory use [8][9]. | Very fast parser and generator in scalar (non‑SIMD) benchmarks with fine‑grained control over memory allocators [7][8][9][12]. | Lower‑level, more verbose API, and core feature set has changed relatively slowly since 1.1.0 (2016) [8].                                                                        |        ~13k  | v1.1.0 (2016) with ongoing maintenance commits [8].    |      11 |
| simdjson     | https://github.com/simdjson/simdjson | SIMD‑accelerated parser with DOM and on‑demand APIs designed for GB/s parsing [5][6][17]. | Highest parse throughput in multiple benchmarks on supported CPUs and strong UTF‑8 validation guarantees [5][6][7][12][17]. | More complex build and configuration; benefits are largest on modern SIMD‑capable CPUs and parse‑bound workloads [5][6][12][17].                                                |        ~23k  | 3.x–4.0.x series 2021–2024 [5].                        |      11 |
| JsonCpp      | https://github.com/open-source-parsers/jsoncpp | Mature DOM‑centric library widely packaged in OS and build ecosystems [10]. | Very widely available via Linux distributions, vcpkg, Conan, and other package managers [10][14][16].                       | Older API design and generally weaker performance than RapidJSON, simdjson, and Boost.JSON in public benchmarks [10][12][13].                                                     |       ~8.8k  | 1.9.5–1.9.6 series (2020–2022) [10].                   |      11 |
| taoJSON      | https://github.com/taocpp/json      | Policy‑driven JSON library with strong validation and multiple encodings [11].   | Highly configurable policies and support for formats such as CBOR and MsgPack alongside JSON [11].                         | Requires C++17 and has a comparatively small, niche community and ecosystem [11][15].                                                                                            |        ~0.7k | 1.0.0‑beta.x series (ongoing) [11].                    |      17 |

\*Star counts are rounded from GitHub as of 2024‑10 [2][3][5][8][10][11][15]. As a rough reference, GitHub lists about 24k dependents for nlohmann/json and under 300 for Boost.JSON as of 2024‑10 [2][3][15].

A counter‑point to Boost.JSON’s Boost integration is that projects not already using Boost may see this as an extra dependency and build‑time cost compared with single‑header libraries such as nlohmann/json [1][3], while projects already standardized on Boost may value this dependency alignment.

## 2 Quantitative comparison

### 2.1 Performance and build impact

Throughput values are taken from json_performance, nativejson‑benchmark, and related work, with additional qualitative evidence from other benchmarks [7][12][13][17].

| Library       | Parse speed (MB/s, DOM)* | Notes on runtime performance                                                                 | Relative DOM memory use (qual.)                                                          | Build‑time impact (qual.)                                                                                                                                       |
|---------------|-------------------------:|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Boost.JSON    |                    ~308  | Solid performance; slower than RapidJSON but faster than nlohmann/json in json_performance on example datasets [7]. | Medium; supports custom allocators and string storage options, but no cross‑library memory‑usage benchmark is published for identical datasets [1][2][7][12]. | Medium; depends on Boost headers and templates, and is distributed as part of Boost rather than as a single header [1][2].                                                                            |
| nlohmann/json |                     ~81  | Clearly slower than Boost.JSON and RapidJSON in json_performance and nativejson‑benchmark DOM tests [7][12]. | Medium‑high due to flexible, variant‑like DOM [3][4][12].                               | High; header‑only and template‑heavy, with benchmarks reporting longer build times than RapidJSON and similar to or above simdjson in optimized builds [7][12]. In very small utilities, overall build complexity can be acceptable or lower than for separate compiled libraries because no external library build or link step is needed, but systematic comparative measurements are scarce [3][4][12]. |
| RapidJSON     |                    ~416  | Faster than Boost.JSON and nlohmann/json on shared datasets in multiple benchmarks [7][12][13]. | Medium with in‑place parsing options and custom allocators [8][9].                      | Medium; header‑only but with a smaller template surface than nlohmann/json in typical usage [8][9][12].                                                                                               |
| simdjson      |                ~1100–1200 | On‑demand API often above 4× RapidJSON and above 10× nlohmann/json on large files on supported CPUs [5][6][7][12][17]. | Low–medium via on‑demand DOM and structural indices [5][6][17].                         | Medium‑high to high; multiple SIMD back ends and dispatch logic, though as a compiled library it can amortize template costs and benefit from separate compilation [5][6][12][17].                     |
| JsonCpp       |                       ~60 | Slower than RapidJSON and nlohmann/json in nativejson‑benchmark; parse speeds typically in the tens of MB/s [12][13]. | Medium [10][12].                                                                         | Medium; traditional compiled library with smaller header surface and less template use than heavily generic header‑only libraries, but no direct multi‑library compile‑time comparisons were located [10][12]. |
| taoJSON       |                        — | Designed for performance and correctness, but few neutral comparative benchmarks published; examples show competitive performance but not GB/s scale [11]. | Medium [11].                                                                             | Medium; template and policy‑heavy design, but split into multiple headers rather than a single monolithic header [11].                                                                                |

\*Numbers approximate DOM parse throughput on representative datasets in cited benchmarks [7][12][13][17]; actual results vary with compiler, flags, CPU, and data.

Allocator control is not unique to Boost.JSON: RapidJSON exposes user‑provided allocators for DOM and parsing [8][9], simdjson allows custom allocators in some higher‑level layers [5][6], and taoJSON uses allocator‑aware containers and policies [11]. Boost.JSON’s allocator story is therefore primarily an advantage for projects already aligned with Boost or pmr rather than a unique feature [1][2][5][8][11].

### 2.2 Code quality and ecosystem

Values are approximate; coverage percentages are only included when explicitly published or exposed via badges or documentation.

| Library       | Approx core LOC (cloc, qual.) | Test coverage info                                   | Notable QA practices                                                           | Stars approx | Contributors approx | Issue response tempo (qual.)                        |
|---------------|-------------------------------:|------------------------------------------------------|--------------------------------------------------------------------------------|-------------:|--------------------:|----------------------------------------------------|
| Boost.JSON    |                        ~20k    | Coverage tracked via Boost CI; no single aggregate percent in repo [1][2]. | Extensive unit tests, benchmarks, fuzzing, and security‑focused testing described in docs [1][2]. |        ~0.5k |                 ~40 | Many issues handled within days to weeks in 2022–2024 [2][15].          |
| nlohmann/json |                        ~40k+   | Coverage badge reports high coverage of core code paths (over 90% on some runs) [3]. | Large test suite, fuzzing, sanitizers, and wide CI matrix across compilers and OSes [3][4]. |        ~48k  |                300+ | Often hours to days for active issues, with some longer‑running items [3][15]. |
| RapidJSON     |                        ~40k    | No numeric coverage in repo, but substantial Google Test suites [8]. | Unit tests, example programs, and long‑term production use at Tencent and others [8][9].     |        ~13k  |                200+ | Typically days to weeks, with a steady though moderate maintenance cadence [8][15]. |
| simdjson      |                        ~15k    | Documentation and papers describe extensive testing of core parser logic [5][6][17]. | Heavy benchmarking, reproducible experiments, multi‑platform CI, and academic evaluation [5][6][17]. |        ~23k  |                160+ | Often hours to days for new issues and PRs [5][15].                      |
| JsonCpp       |                        ~15k    | No public percentage; has regression tests and examples [10]. | Unit tests and long‑term use in many systems and distributions [10][14][16].                 |       ~8.8k  |                200+ | Frequently weeks for resolution, consistent with a stable, low‑churn project [10][15]. |
| taoJSON       |                        ~20k    | No numeric coverage, but extensive tests in repo [11]. | Strong emphasis on invariants and validation; defensive programming in examples [11].        |        ~0.7k |                 <10 | Many issues addressed over days to weeks, with lower overall issue and PR volume than larger projects [11][15]. |

Issue tempos are rough observations from 2022–2024 issue histories and GitHub insights [2][3][5][8][10][11][15]; they do not attribute causes such as maintainer count, and individual issues may deviate significantly from these patterns.

### 2.3 Standards, portability, and usability

Ergonomics and documentation scores are relative, subjective ratings within this set, based on API design, examples, and documentation depth as of 2024‑10.

| Library       | Min C++ | Platform and OS support (evidence)                                     | API ergonomics 1–5 | Documentation 1–5 |
|---------------|--------:|------------------------------------------------------------------------|--------------------|-------------------|
| Boost.JSON    |      11 | Major desktop and server platforms via Boost build and test matrix [1][2]. | 4                  | 4                 |
| nlohmann/json |      11 | Very wide; used across Linux, Windows, macOS; packaged by many managers [3][4][14][16]. | 5                  | 5                 |
| RapidJSON     |      11 | Cross‑platform including embedded targets; CI on multiple OSes [8][9]. | 3                  | 4                 |
| simdjson      |      11 | x86_64, ARM, POWER with SIMD, tested on major OSes in CI [5][6][17].   | 3                  | 4                 |
| JsonCpp       |      11 | Widely available via vcpkg, Conan, and distro packages [10][14][16].  | 3                  | 3                 |
| taoJSON       |      17 | Standard desktop and server toolchains with C++17 or later [11].      | 4                  | 4                 |

nlohmann/json scores highest on ergonomics here due to implicit conversions, STL‑like containers, and single‑header integration [3][4], but some maintainers prefer more explicit APIs (RapidJSON, taoJSON, Boost.JSON) to better control implicit conversions, binary size, and error handling in large codebases [1][2][8][11][12].

## 3 Trends 2023–2024

- **Boost.JSON**  
  - Continues to evolve with regular Boost releases, emphasizing robustness, fuzzing, and security‑related testing; commits and issues remain active though smaller in volume than nlohmann/json [1][2][15].  
  - Stars and GitHub dependents grow steadily but remain an order of magnitude below nlohmann/json, suggesting slower visible open‑source adoption; internal Boost and proprietary usage is not reflected in these public metrics [1][2][3][15].

- **nlohmann/json**  
  - Maintains frequent 3.x releases and very active issue and PR activity, with many external contributors [3][4][15].  
  - Strong adoption trajectory evidenced by star growth, many thousands of dependents, and wide availability in vcpkg, Conan, and distro repositories [3][4][14][16].

- **RapidJSON**  
  - Feature growth is modest since 1.1.0, with most changes being fixes and maintenance, but existing deployments remain numerous [8][15].  
  - Benchmarks and industrial users continue to include RapidJSON as a baseline, though newer high‑performance work often focuses on simdjson for peak throughput [5][6][12][13][17].

- **simdjson**  
  - Rapid adoption driven by clear performance advantages in academic and independent benchmarks, and bindings in other languages [5][6][12][13][17].  
  - Active release cadence in the 3.x–4.x series, with ongoing tuning and API refinements, and documented usage in databases and analytics systems [5][6][17].

- **JsonCpp**  
  - Stable and low‑churn; most recent changes are minor bug fixes in the 1.9.x line [10].  
  - Still entrenched via OS packages and build systems, but less commonly chosen for new performance‑sensitive projects, based on benchmark comparisons and GitHub trend lines [10][12][14][16].

- **taoJSON**  
  - Niche but steady, focused on correctness, policy‑based design, and multiple encodings [11].  
  - Star and contributor counts grow slowly; activity is concentrated in a small core team, with fewer external PRs than the larger projects [11][15].

## 4 When to use Boost.JSON vs alternatives

### 4.1 Summary decision table

| Library       | Main advantage vs Boost.JSON                                                           | Main disadvantage vs Boost.JSON                                              | When to prefer                                                                                               | C++ standard |
|---------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------:|
| Boost.JSON    | Balanced performance, allocator control, and seamless integration with other Boost libs [1][2]. | Depends on Boost and has lower standalone GitHub stars and dependents [2][3][15]. | Boost‑centric C++11 applications needing good speed, memory control, and consistent error handling.          |          11 |
| nlohmann/json | Very ergonomic STL‑like API and the largest GitHub community and ecosystem in this set [3][4][15]. | Slower and heavier at compile time than Boost.JSON and RapidJSON in benchmarks, and slower at run time than RapidJSON and simdjson [7][12]. | Application‑level code where developer productivity and readability outweigh raw performance and build times, especially when a single header and wide packaging support are helpful. |          11 |
| RapidJSON     | Higher scalar throughput in many DOM and SAX benchmarks with fine‑grained allocator control [7][8][9][12]. | Lower‑level API and relatively slow feature evolution [8].                   | Performance‑critical components that want non‑SIMD speed and accept a more verbose API.                      |          11 |
| simdjson      | Highest parse throughput on modern CPUs and strong UTF‑8 validation [5][6][7][12][17]. | More complex build and can be overkill for small or infrequent JSON loads [5][6][12]. | High‑throughput services, log pipelines, and analytics backends where parsing dominates CPU time.            |          11 |
| JsonCpp       | Very easy to obtain and integrate on many platforms and build systems [10][14][16].   | Older API design and generally weaker performance and ergonomics [10][12][13]. | Legacy or constrained systems where JsonCpp is already standard or must align with distro packages.          |          11 |
| taoJSON       | Strong validation, policy flexibility, and multi‑format support including CBOR and MsgPack [11]. | Requires C++17 and has a niche ecosystem [11][15].                          | Safety‑critical or heavily validated systems on modern toolchains that value policy control over simplicity. |          17 |

### 4.2 Practical guidance and balanced trade‑offs

- **Prefer Boost.JSON when**  
  - The project already uses Boost components such as Asio or Beast and benefits from shared allocators, error codes, and consistent conventions [1][2].  
  - C++11 compatibility is required and you want a balance of performance and control without adopting SIMD‑specific complexity.

- **Prefer nlohmann/json when**  
  - Readability and minimal friction are primary goals, especially for application‑layer logic and scripting‑style tasks, and when a single header and wide ecosystem support are valuable [3][4][14].  
  - Compile‑time and run‑time overhead are acceptable relative to development speed; where they are not, RapidJSON, Boost.JSON, or simdjson often provide leaner alternatives in benchmarks [7][12].

- **Prefer RapidJSON or simdjson when**  
  - Maximizing parse speed is critical; RapidJSON is a strong default on scalar CPUs with familiar DOM and SAX APIs, while simdjson dominates on modern SIMD hardware and large datasets [5][6][7][8][9][12][13][17].  
  - All of these, including Boost.JSON and taoJSON, support custom allocators, so the choice is more about ecosystem fit, performance goals, and API style than allocator capability alone [1][2][5][8][11].

- **Prefer JsonCpp or taoJSON when**  
  - JsonCpp is the default in your platform or distribution and replacing it would introduce risk or significant maintenance work, despite moderate performance [10][12][14][16].  
  - taoJSON is desired for its validation guarantees, policy‑based customization, and binary format support in C++17 codebases, accepting a smaller community and fewer benchmarks in exchange [11].

Overall, Boost.JSON is a strong choice for Boost‑based C++11 projects that value integration and solid performance, while nlohmann/json leads in usability and ecosystem breadth, simdjson in raw parsing speed, RapidJSON in non‑SIMD performance and control, and JsonCpp and taoJSON occupy stable legacy and high‑validation niches respectively.

### Sources

[1] Boost.JSON documentation: https://www.boost.org/doc/libs/release/libs/json/doc/html/index.html  
[2] Boost.JSON GitHub repository: https://github.com/boostorg/json  
[3] nlohmann/json GitHub repository: https://github.com/nlohmann/json  
[4] nlohmann/json documentation: https://json.nlohmann.me  
[5] simdjson GitHub repository: https://github.com/simdjson/simdjson  
[6] simdjson documentation and performance overview: https://simdjson.org  
[7] json_performance benchmark: https://github.com/stephenberry/json_performance  
[8] RapidJSON GitHub repository: https://github.com/Tencent/rapidjson  
[9] RapidJSON documentation: https://rapidjson.org  
[10] JsonCpp GitHub repository: https://github.com/open-source-parsers/jsoncpp  
[11] taocpp/json GitHub repository and docs: https://github.com/taocpp/json  
[12] nativejson‑benchmark (multi‑library C++ JSON benchmark): https://github.com/miloyip/nativejson-benchmark  
[13] kostya/benchmarks JSON tests: https://github.com/kostya/benchmarks  
[14] vcpkg ports for JSON libraries: https://github.com/microsoft/vcpkg/tree/master/ports  
[15] GitHub insights for stars, contributors, and dependents (accessed 2024‑10).  
[16] ConanCenter and distro packaging references for nlohmann/json and JsonCpp: https://conan.io/center and distribution package indices (Debian, Fedora, etc.).  
[17] G. Langdale, D. Lemire, Parsing Gigabytes of JSON per Second, VLDB 2019 and subsequent simdjson performance materials (linked from simdjson repo and site).