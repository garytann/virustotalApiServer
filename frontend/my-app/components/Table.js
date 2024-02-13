'use client';

import React, { useEffect } from 'react';
import { Space, Table, Tag } from 'antd';
const { Column, ColumnGroup } = Table;
import { UploadOutlined } from '@ant-design/icons';
import { InboxOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';


export default function DataTable() {

    const [dataSource, setDataSource] = React.useState([]);
    const { Dragger } = Upload;

    const props = {
        name: 'file',
        // multiple: true,
        // action: 'http://103.3.61.201:3000/api/upload'
        action: 'http://localhost:3000/api/upload',
        headers: {
            authorization: 'authorization-text',
        },
        onChange(info) {
            const { status } = info.file;
            if (status !== 'uploading') {
                console.log(info.file, info.fileList);
            }
            if (status === 'done') {
                message.success(`${info.file.name} file uploaded successfully.`);
                setDataSource(info.file.response.data);
            } else if (status === 'error') {
                message.error(`${info.file.name} file upload failed.`);
            }
        },
        onDrop(e) {
            console.log('Dropped files', e.dataTransfer.files);
        },
    };

    // const props = {
    //     name: 'file',
    //     action: 'http://localhost:3000/api/upload',
    //     headers: {
    //         authorization: 'authorization-text',
    //     },
    //     async onChange(info) {
    //         if (info.file.status !== 'uploading') {
    //             console.log(info.file, info.fileList);
    //             console.log("hello world");
    //         }
    //         if (info.file.status === 'done') {
    //             message.success(`file uploaded successfully`);
    //             // console.log('##info', info.file.response.data);
    //             setDataSource(info.file.response.data);

    //         } else if (info.file.status === 'error') {
    //             message.error(`file upload failed.`);
    //         }
    //     },
    // };

    const [column] = React.useState([
        {
            title: 'ID',
            dataIndex: 'analysis_id',
            key: 'analysis_id',
        },
        {
            title: 'File',
            dataIndex: 'filename',
            key: 'filename',
        },
        {
            title: 'SHA256',
            dataIndex: 'hash_id',
            key: 'hash_id',
        },
        {
            title: 'Detected',
            dataIndex: 'type',
            key: 'type',
        },
        {
            title: 'Date',
            dataIndex: 'date',
            key: 'date',
        }
    ]);

    // const [file, setFile] = React.useState(null);

    // const handleFileChange = (e) => {
    //     console.log('hello world')
    //     setFile(e.target.files[0]);
    // };


    // handle the file upload
    // const uploadFile = async () => {
    //     try {
    //         const formData = new FormData();
    //         formData.append('file', file);
    //         const res = await fetch('/api/upload', {
    //             method: 'POST',
    //             body: formData,
    //         }).then((res) => { console.log("data", res) });
    //         const response = await res.json();

    //         // console.log("helloworld");
    //         // console.log('##response', response);

    //     } catch (error) {
    //         console.error('Error uploading:', error);
    //     }
    // };

    return (
        <div>
            {/* <Upload onSubmit={handleFileChange} {...props}> */}
            {/* <Upload {...props} showUploadList={false}>
                <Button icon={<UploadOutlined />}>Click to Upload</Button>
            </Upload> */}

            <Dragger {...props} showUploadList={false}>
                <p className="ant-upload-drag-icon">
                    <InboxOutlined />
                </p>
                <p className="ant-upload-text">Click or drag file to this area to upload</p>
                <p className="ant-upload-hint">
                    Support for a single upload ONLY. Strictly prohibited from uploading company data or other
                    banned files.
                </p>
            </Dragger>

            <Table dataSource={dataSource} columns={column}>
                {/* <Column title="ID" dataIndex="analysis_id" key="analysis_id" />
                <Column title="File" dataIndex="filename" key="filename" />
                <Column title="SHA256" dataIndex="hash_id" key="hash_id" />
                <Column title="Detected" dataIndex="type" key="type" />
                <Column title="Date" dataIndex="date" key="date" /> */}
            </Table>

        </div>
    );

};
