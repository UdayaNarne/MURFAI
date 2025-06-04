// Function to get selected text
function getSelectedText() {
    return window.getSelection().toString().trim();
  }
  
  // Function to highlight selected text in light blue
  function highlightSelection() {
    const selection = window.getSelection();
    if (!selection.rangeCount) return;
  
    const range = selection.getRangeAt(0);
    if (selection.toString().length > 0) {
      const span = document.createElement('span');
      span.style.backgroundColor = 'pink';
  
      try {
        // Wrap selected content in span
        range.surroundContents(span);
        // Clear selection so user sees highlight without selection markers
        selection.removeAllRanges();
      } catch (e) {
        console.error("Could not highlight selection:", e);
        // fallback or ignore
      }
    }
  }
  
  // Listen for a message from background when icon clicked
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "readSelectedText") {
      const text = getSelectedText();
      if (text) {
        highlightSelection(); // Highlight only if some text is selected
      }
      sendResponse({ text }); // send back the selected text
    }
  });
  