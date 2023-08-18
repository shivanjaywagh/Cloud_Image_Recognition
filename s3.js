const AWS = require('aws-sdk');
const { request, response } = require('express');
const s3 = new AWS.S3();

const fs = require('fs');
const s3uploadfun = (request,respond) =>{
const fileStream = fs.createReadStream(request.file.path);

const params = {
  Bucket: '',
  Key: request.file.originalname,
  Body: fileStream,
};

return s3.upload(params).promise();

}
exports.s3uploadfun=s3uploadfun;