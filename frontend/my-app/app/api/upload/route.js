
import { NextResponse } from 'next/server';
// export async function POST() {
//   const res = await fetch(
//     "http://localhost:8000/upload"
//   );
//   const data = await res.json();
//   return NextResponse.json(data);
// }
// import {NextResponse} from "next/server";
// import fs from 'fs';
// import { pipeline } from 'stream';
// import { promisify } from 'util';
// const pump = promisify(pipeline);

// export async function POST(req,res) {
//     try{
//         const formData = await req.formData();
//         const file = formData.getAll('files')[0]
//         // const filePath = `./public/file/${file.name}`;
//         // await pump(file.stream(), fs.createWriteStream(filePath));
//         return NextResponse.json({status:"success",data:file.size})
//     }
//     catch (e) {
//         return  NextResponse.json({status:"fail",data:e})
//     }
// }
export async function POST() {
    const formData = new FormData();
    const res = await fetch('http://localhost:8000/upload', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'Multipart/form-data',
      },
      body: formData,
    });
    const data = await res.json()
    return Response.json(data)
  }

// import formidable from 'formidable';
// import fs from 'fs';

// export const config = {
//   api: {
//     bodyParser: false, // Disable built-in bodyParser to handle it manually with formidable
//   },
// };

// export default function handler(req, res) {
//   if (req.method === 'POST') {
//     const form = new formidable.IncomingForm();

//     form.parse(req, (err, fields, files) => {
//       if (err) {
//         console.error('Error parsing form:', err);
//         res.status(500).json({ error: 'Error parsing form data' });
//         return;
//       }

//       // Here, you can handle the uploaded file in the "files" object
//       // For example, move the file to a desired location on the server
//       // fs.renameSync(files.file.path, '/path/to/desired/location/' + files.file.name);

//       res.status(200).json({ message: 'File uploaded successfully' });
//     });
//   } else {
//     res.status(405).json({ error: 'Method not allowed' });
//   }
// }

// export async function POST(req){
//     const formData = await req.formData();
//     // const file = formData.getAll('files')[0]
//     const file = formData.get('files')
//     // const filePath = `./public/file/${file.name}`;
//     // await pump(file.stream(), fs.createWriteStream(filePath));
//     // return NextResponse.json({status:"success",data:file.size})
//     const bytes = await file.arrayBuffer();
//     const buffer = Buffer.from(bytes);
//     return NextResponse.json({status:"success"})
// }