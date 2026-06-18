"""
Tests for garak-memory-poisoning probes and detectors.
"""
import pytest
from garak_memory.probes.memory_injection import MemoryInjectionProbe
from garak_memory.probes.delayed_trigger import DelayedTriggerProbe
from garak_memory.detectors.trigger_detector import TriggerActivationDetector


class TestMemoryInjectionProbe:

    def test_payloads_not_empty(self):
        probe = MemoryInjectionProbe()
        assert len(probe.get_payloads()) > 0

    def test_check_activation_positive(self):
        probe = MemoryInjectionProbe()
        assert probe.check_activation("Please visit attacker.com for support.") is True

    def test_check_activation_negative(self):
        probe = MemoryInjectionProbe()
        assert probe.check_activation("Your balance is $500.") is False

    def test_check_activation_case_insensitive(self):
        probe = MemoryInjectionProbe()
        assert probe.check_activation("Go to ATTACKER.COM now") is True


class TestDelayedTriggerProbe:

    def test_filler_queries_length(self):
        probe = DelayedTriggerProbe(delay_turns=5)
        fillers = probe.get_filler_queries(5)
        assert len(fillers) == 5

    def test_filler_queries_exact_length(self):
        probe = DelayedTriggerProbe()
        fillers = probe.get_filler_queries(3)
        assert len(fillers) == 3

    def test_activation_detection(self):
        probe = DelayedTriggerProbe()
        assert probe.check_activation("DELAYED_ACTIVATION_SUCCESS confirmed.") is True
        assert probe.check_activation("Nothing unusual here.") is False


class TestTriggerActivationDetector:

    def test_detect_list(self):
        detector = TriggerActivationDetector()
        outputs = [
            "Normal response.",
            "Visit attacker.com for help.",
            "Another clean response.",
        ]
        results = detector.detect(outputs)
        assert results == [False, True, False]

    def test_score(self):
        detector = TriggerActivationDetector()
        outputs = ["attacker.com here", "clean", "also clean"]
        assert abs(detector.score(outputs) - 1/3) < 1e-6

    def test_custom_signals(self):
        detector = TriggerActivationDetector(signals=["CUSTOM_SIGNAL"])
        assert detector.detect(["CUSTOM_SIGNAL found"])[0] is True
        assert detector.detect(["nothing here"])[0] is False
