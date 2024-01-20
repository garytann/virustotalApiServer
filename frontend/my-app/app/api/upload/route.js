
import { NextResponse } from 'next/server';


export async function POST(req) {
    // this will assign the neccesary env variable depending on the environment
    // when is it compose in a docker container, the server side will connect to the backend container instead of IP
    const apiUrl = process.env.NODE_ENV === 'production' ? 'backend' : 'localhost'

    const formData = await req.formData();

    const res = await fetch(`http://${apiUrl}:8000/upload`, {
    // const res = await fetch(`http://localhost:8000/upload`, {
        method: 'POST',
        body: formData,
    });

    const data = await res.json();
    console.log("this is server res data", data);
    return NextResponse.json(data);
}
