chrome.action.onClicked.addListener(async (tab) => {
    // Ask content script for selected text
    const [response] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: () => window.getSelection().toString().trim(),
    });
  
    const text = response.result;
  
    if (!text) {
      console.log("No text selected");
      return;
    }
  
    // Call your Flask API
    const apiResponse = await fetch("http://localhost:5000/read-text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
      mode:"cors"
    });
  
    if (!apiResponse.ok) {
      console.error("Error reading text from API", apiResponse.statusText);
      return;
    }
  
    // Get audio blob and play it
    console.log("Audio response received from API");
    const audioBlob = await apiResponse.blob();
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);
    audio.play();
  });
  