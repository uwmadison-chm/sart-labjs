# Sustained Attention to Response Task for lab.js

A online SART implementation in lab.js.

## Hosting in Qualtrics

See the [Lab.js documentation on working with Qualtrics](https://labjs.readthedocs.io/en/latest/learn/deploy/3a-qualtrics.html).

Then, when pasting the embed source, change the iframe src to pass participant 
id and session variables like this:

    <iframe
      src="//some-location?PPT=${e://Field/PPTID}&session=${e://Field/session}"
      style="width: 100%; min-height: 600px; border: none;"
    ></iframe>


