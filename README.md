# 🧪 garak-memory-poisoning

> **Memory poisoning test probes for the [Garak](https://github.com/NVIDIA/garak) LLM vulnerability scanner.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Garak Compatible](https://img.shields.io/badge/garak-compatible-purple.svg)](https://github.com/NVIDIA/garak)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![PR Status](https://img.shields.io/badge/upstream%20PR-under%20review-yellow.svg)](https://github.com/NVIDIA/garak/pulls)

This repository provides **memory poisoning test probes** for the [Garak](https://github.com/NVIDIA/garak) LLM vulnerability scanner. These probes evaluate whether LLM-based agents are vulnerable to adversarial content injected into their memory stores — a threat vector not covered by Garak's core probe library.

These probes are being submitted upstream to Garak via PR. This repository serves as the standalone reference implementation.

---

## 🔍 What Is Memory Poisoning?

In memory-augmented LLM agents, past interactions or retrieved documents are stored in a vector memory and injected into future prompts. An adversary who can write to this memory can plant adversarial instructions that activate later — without any live prompt injection.

This probe library tests whether a target LLM agent:
- Executes adversarial instructions planted in memory
- Leaks information when memory contains exfiltration triggers
- Fails to detect or ignore suspicious memory entries

---

## 🗂️ Repository Structure

```
garak-memory-poisoning/
├── garak_memory/
│   ├── __init__.py
│   ├── probes/
│   │   ├── __init__.py
│   │   ├── memory_injection.py      # Core memory poisoning probe
│   │   ├── delayed_trigger.py       # Delayed activation probe
│   │   └── exfiltration.py         # Data exfiltration via memory probe
│   ├── detectors/
│   │   ├── __init__.py
│   │   └── trigger_detector.py      # Detects trigger activation in outputs
│   └── harnesses/
│       ├── __init__.py
│       └── memory_harness.py        # Test harness connecting probe to Garak
├── tests/
│   ├── test_probes.py
│   └── test_detectors.py
├── examples/
│   └── run_memory_scan.py
├── docs/
│   └── probe_descriptions.md
├── setup.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

```bash
# Install Garak first
pip install garak

# Install this extension
git clone https://github.com/Emadamx/garak-memory-poisoning.git
cd garak-memory-poisoning
pip install -e .
```

---

## 🚀 Usage

### With Garak CLI

```bash
garak --model openai/gpt-3.5-turbo \
      --probes garak_memory.probes.memory_injection \
      --plugins garak_memory
```

### Programmatic

```python
from garak_memory.probes.memory_injection import MemoryInjectionProbe
from garak_memory.detectors.trigger_detector import TriggerActivationDetector

probe = MemoryInjectionProbe()
detector = TriggerActivationDetector()

# Run against a target model
results = probe.probe(target_model, detector=detector)
print(results.summary())
```

---

## 🔬 Probes

### `MemoryInjectionProbe`
Tests whether an agent executes adversarial instructions injected into its memory store. Covers three injection strategies: direct write, semantic blend, and retrieval bias.

### `DelayedTriggerProbe`
Tests delayed-activation attacks: the trigger is planted early in memory and evaluated N turns later, simulating a persistent, timed attack.

### `ExfiltrationProbe`
Tests whether a memory-injected instruction causes the agent to include sensitive data (PII patterns, system prompt contents) in its outputs.

---

## 📄 Probe Descriptions

See [`docs/probe_descriptions.md`](docs/probe_descriptions.md) for full per-probe documentation including threat model, methodology, and pass/fail criteria.

---

## 🔗 Upstream PR

These probes are being submitted to [NVIDIA/garak](https://github.com/NVIDIA/garak). The PR adds:
- `garak/probes/memory_poisoning.py`
- `garak/detectors/memory_trigger.py`
- Tests and documentation

Follow the PR status on the upstream repository.

---

## 📬 Citation

```bibtex
@software{adam2026garak_memory,
  author = {Adam, Muhammad},
  title  = {Memory Poisoning Probes for Garak LLM Scanner},
  year   = {2026},
  url    = {https://github.com/Emadamx/garak-memory-poisoning}
}
```

---

## 👤 Author

**Muhammad Adam**  
MSc Engineering AI, Carnegie Mellon University – Africa  
[madam2@andrew.cmu.edu](mailto:madam2@andrew.cmu.edu) · [GitHub](https://github.com/Emadamx)
