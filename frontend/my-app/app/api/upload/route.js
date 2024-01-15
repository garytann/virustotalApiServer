
import { NextResponse } from 'next/server';

export async function POST(req) {
    // const formData = new FormData();
    // ipmport to use this to set the file data that receive from client
    const formData = await req.formData();
    // const fileInput = req.files.file; // Assuming the file input field name is "file"

    // formData.append('file', fileInput);

    const res = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
    });

    const data = await res.json();
    console.log("this is server res data", data);
    return NextResponse.json(data);
}
