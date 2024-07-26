#target photoshop

// Function to read lines from a CSV file
function readCSVFile(filePath) {
    var file = new File(filePath);
    var lines = [];

    if (file.exists) {
        file.open('r');
        
        while (!file.eof) {
            var line = file.readln();
            lines.push(line);
        }
        file.close();
    } else {
        throw new Error("CSV file not found: " + filePath);
    }

    return lines;
}

// Define the path to your CSV file
var csvFilePath = "B:/personal folders/automatic_quran_vids/text_entries.csv"; // Change this path to your CSV file

// Read text entries from the CSV file
var textEntries = readCSVFile(csvFilePath);

// Open the template file
var templateFile = new File("B:/personal folders/automatic_quran_vids/template.psd"); // Change this path to your template file
if (!templateFile.exists) {
    alert("Template file not found. Check the file path.");
    throw new Error("Template file not found");
}
app.open(templateFile);

// Get the active document (the template)
var doc = app.activeDocument;

// Check if the text layer exists
var textLayer;
try {
    textLayer = doc.artLayers.getByName("TextLayer");
} catch (e) {
    alert("Text layer 'TextLayer' not found. Check the layer name in your template.");
    throw new Error("Text layer 'TextLayer' not found");
}

// Loop through the text entries and create new images
for (var i = 0; i < textEntries.length; i++) {
    // Change the text layer
    textLayer.textItem.contents = textEntries[i];
    
    // Save the new image
    var outputFilePath = "B:/personal folders/automatic_quran_vids/output_img/image_" + (i + 1) + ".jpg"; // Change the output directory and file naming as needed
    var outputFile = new File(outputFilePath);
    var options = new JPEGSaveOptions();
    options.quality = 12; // Set the quality from 0 to 12 (12 being the highest quality)
    try {
        doc.saveAs(outputFile, options, true, Extension.LOWERCASE);
        alert("Saved: " + outputFilePath);
    } catch (e) {
        alert("Failed to save: " + outputFilePath + ". Error: " + e.message);
    }
}

// Close the document without saving changes to the template



doc.close(SaveOptions.DONOTSAVECHANGES);
alert("Script completed.");
