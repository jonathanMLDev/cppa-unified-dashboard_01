# Top 20 Companies That Avoid Using MIT-Licensed Code in Standard Library Implementations Due to Binary Attribution Requirements

## Overview

Companies developing C++ compilers and standard libraries avoid MIT-licensed code because the MIT license requires copyright notices in binary distributions, creating compliance burdens for end users. Licenses like BSL (Boost Software License) are preferred as they exempt binary attribution requirements.

## Companies List

Here's a list of top companies involved in developing or distributing C++ compilers and standard libraries, where this attribution challenge applies (ranked roughly by market influence in tech/hardware):

1. **Microsoft** - Maintains MSVC STL; explicitly avoids MIT due to binary attribution burdens on users.
2. **Apple** - Uses and contributes to libc++ (LLVM-based); prefers licenses like BSL or Apache with exceptions for binary distributions.
3. **Google** - Relies on Clang/libc++ for Android NDK; avoids licenses imposing downstream attribution.
4. **Intel** - Develops oneAPI DPC++/C++ Compiler; focuses on compatible licenses for hardware-optimized libraries.
5. **IBM** - Maintains OpenXL (LLVM-based); adheres to strict policies for runtime inclusions.
6. **Oracle** - Provides Oracle Developer Studio compilers; avoids complicating binary distributions.
7. **NVIDIA** - Develops nvcc compiler; integrates with CUDA runtimes where attribution cascades are problematic.
8. **AMD** - Uses LLVM for ROCm compilers; prefers exemption-heavy licenses for GPU toolchains.
9. **ARM Holdings** - Offers Arm Compiler; focuses on embedded systems where binary notices are burdensome.
10. **Qualcomm** - Provides toolchains for Snapdragon; avoids licenses affecting downstream embedded binaries.
11. **Broadcom** - Involved in chip toolchains; similar concerns in hardware-software integration.
12. **Texas Instruments** - Develops TI compilers for embedded devices; binary attribution complicates distributions.
13. **Siemens** - Through Mentor Graphics, provides embedded compilers; prefers no-attribution in objects.
14. **Synopsys** - Offers compiler tools for EDA; avoids cascading requirements in design flows.
15. **Cadence Design Systems** - Develops compiler integrations; focuses on clean binary licensing.
16. **Embarcadero Technologies** - Maintains C++Builder (Clang-based); adheres to policies for RAD tools.
17. **Perforce (Rogue Wave)** - Provides legacy compiler components; avoids MIT for library compatibility.
18. **Hewlett Packard Enterprise (Cray)** - Develops Cray compilers; concerns in HPC environments.
19. **Fujitsu** - Offers compilers for supercomputing; prefers BSL-like exemptions.
20. **NEC** - Provides vector engine compilers; similar issues in high-performance runtimes.

## Notes on Accuracy

- Microsoft's STL team has publicly discussed MIT license concerns regarding binary attribution requirements.
- The general principle about MIT license binary attribution requirements is accurate, though specific company policies may vary.
- Some companies listed may have evolved their licensing policies over time.
- The ranking is approximate and based on general market influence rather than strict metrics.
