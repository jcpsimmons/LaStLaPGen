# LaStLaPGen
Living Spaces Landing Page Generator

Creating the initial scaffolding for landing pages on the Living Spaces website can be tedious. To give our designers maximum leeway in their designs, we typically build landing pages with flex as opposed to a framework like Bootstrap (although the site does have Bootstrap 3 and we do use some of its features).

The first thing I do when I get a landing page is break it apart into columns and rows so I can scaffold my divs to be filled with content as I code along.

After I put this scaffolding together, I realize I haven't saved the HTML file. I create a folder with the date (year first) so I can easily look through my archives later. Then I create an img folder in that folder to put optimized images for the site (which I do one by one with Squoosh).


LaStLaPGen automates most of this process, here's an overview of what it does:
- Creates folder structure for new webpage with my naming convention
- Optimizes all images to be used and moves them to an img subfolder
- Generates all rows and columns in HTML (each with a unique class name for easy styling later)
- Adds HTML for linked images in the areas where that needs to be done
- Optionally adds a YouTube video thumbnail with a jQuery-handled popup modal, complete with YouTube link

---

After the aforementioned stages, I only have to add text, put 'flex-basis' for sizing, and hide/reveal various elements for mobile (the generated CSS comes complete with desktop-only and mobile-only classes for hiding and showing elements).

As I continue to work on this software, I hope to add flex-basis capability to the script, and automatic image uploading to our CMS - where we are hosting our images.
