
import { NextResponse } from 'next/server';


export async function POST(req) {
    const formData = await req.formData();

    const res = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
    });

    const data = await res.json();
    console.log("this is server res data", data);
    return NextResponse.json(data);
}
