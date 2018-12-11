import datetime

from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, \
    StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MuxingStream, CloudRegion, ProgressiveWebMMuxing, VP9CodecConfiguration, OpusCodecConfiguration, VP9Quality
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT_YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example webm encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1,
                        encoder_version='BETA')

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = VP9CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                            bitrate=4800000,
                                                            rate=25.0,
                                                            width=1920,
                                                            height=1080,
                                                            tile_columns=2,
                                                            quality=VP9Quality.GOOD)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.VP9.create(video_codec_configuration_1080p).resource

    audio_codec_configuration = OpusCodecConfiguration(name='example_audio_codec_configuration_english',
                                                       bitrate=128000,
                                                       rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.Opus.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream], name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    webm_muxing_output = EncodingOutput(output_id=s3_output.id,
                                        output_path=OUTPUT_BASE_PATH,
                                        acl=[acl_entry])

    webm_muxing = ProgressiveWebMMuxing(streams=[video_muxing_stream_1080p, audio_muxing_stream],
                                        filename='myfile.webm',
                                        outputs=[webm_muxing_output],
                                        name='Sample WebM Muxing 1080p')

    webm_muxing = bitmovin.encodings.Muxing.ProgressiveWebM.create(object_=webm_muxing,
                                                                   encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    print("File successfully encoded")


if __name__ == '__main__':
    main()
