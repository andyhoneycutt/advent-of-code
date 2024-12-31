package Main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	output := Part1()
	if output != "Part 1" {
		t.Errorf("Expected Part 1, got %s", output)
	}
}
