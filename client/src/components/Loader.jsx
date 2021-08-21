import React from 'react'
import { Container, Spinner } from 'react-bootstrap'

const Loader = () => {
    return (
        <Container fluid style={{
            background: "#08061B",
            minHeight:"100vh"
        }} className="d-flex justify-content-center align-items-center h-100 w-100">

        <svg className="loader-logo" width="90" height="90" viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6.11745 5.825L10.7646 9.57489L9.69878 10.6513L6.11745 5.825Z" fill="white"/>
        <path d="M6.03882 14.1051L9.70402 9.35596L10.7593 10.4478L6.03882 14.1051Z" fill="white"/>
        <path d="M14.3347 14.3902L9.68754 10.6403L10.7534 9.56388L14.3347 14.3902Z" fill="white"/>
        <path d="M14.592 5.90908L10.9268 10.6582L9.87149 9.56635L14.592 5.90908Z" fill="white"/>
        <path d="M10.4401 8.24717L10.0135 8.24432C9.93484 8.46628 9.91235 8.6067 9.74474 8.67633C9.5766 8.74623 9.46298 8.66099 9.25585 8.55894L8.95264 8.8648C9.04951 9.0758 9.13249 9.19389 9.06192 9.3651C8.99162 9.53563 8.85289 9.55723 8.63561 9.63448L8.6334 10.07C8.84883 10.1498 8.98824 10.1733 9.05693 10.3449C9.12576 10.5166 9.04253 10.6322 8.94258 10.8438L9.24264 11.1537C9.45013 11.0547 9.56489 10.9706 9.73257 11.0428C9.89998 11.115 9.92128 11.2576 9.99699 11.4784L10.4236 11.4812C10.5013 11.2618 10.5244 11.1191 10.6924 11.0492C10.862 10.9789 10.9782 11.0665 11.1811 11.1666L11.4844 10.8607C11.3874 10.6496 11.3046 10.5315 11.3752 10.3605C11.4455 10.1898 11.5846 10.1682 11.8015 10.0911L11.8037 9.65559C11.5881 9.57573 11.4491 9.55215 11.3798 9.3796C11.3114 9.20908 11.3946 9.09387 11.4946 8.88189L11.1944 8.57194C10.9876 8.67082 10.8723 8.75513 10.7046 8.68299C10.5372 8.61086 10.5157 8.46773 10.4401 8.24717ZM10.7466 9.8663C10.745 10.164 10.5074 10.4037 10.2158 10.4018C9.92419 10.3998 9.689 10.1569 9.69051 9.85927C9.69203 9.5616 9.92968 9.32184 10.2213 9.32378C10.5129 9.32572 10.7481 9.56863 10.7466 9.8663Z" fill="white"/>
        <path d="M0.336914 9.75149L8.1484 8.83015L8.13816 10.8401L0.336914 9.75149Z" fill="white"/>
        <path d="M20.3369 9.97676L12.114 10.8952L12.1243 8.88559L20.3369 9.97676Z" fill="white"/>
        <path d="M10.3685 0L11.2849 7.98338L9.30835 7.97021L10.3685 0Z" fill="white"/>
        <path d="M10.1993 20L9.28283 12.0167L11.2594 12.0298L10.1993 20Z" fill="white"/>
        </svg>
        </Container>
        
    )
}

export default Loader