import Container from './Container';

export default function Footer() {

    return (
        <div className='relative'>
            <Container>
                <h1 className=" flex justify-center item-center uppercase text-xl italic">
                    LOGO
                </h1>
                <div className="flex justify-center items-center h-24">
                    <p className="text-gray-800 my-10 ">Copyright © {new Date().getFullYear()}. Made by {" "}
                        <a className='text-indigo-600 hover:underline'
                            href="https://www.linkedin.com/in/gary-tan-8839b8197/"
                            target="_blank"
                            rel="noopener"
                        >
                            gryt.
                        </a>
                    </p>
                </div>
            </Container>
        </div>
    )
}