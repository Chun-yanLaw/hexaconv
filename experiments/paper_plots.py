import matplotlib.pyplot as plt
import numpy as np
from groupy.plot.plot_p4 import plot_p4
from groupy.plot.plot_p4m import plot_p4m

# Code used to create the figures in
# T.S. Cohen, M. Welling, Group Equivariant Convolutional Networks.
# Proceedings of the International Conference on Machine Learning (ICML), 2016


def paper_plots_p4():
    import matplotlib
    matplotlib.rcParams['ps.useafm'] = True
    matplotlib.rcParams['pdf.use14corefonts'] = True
    matplotlib.rcParams['text.usetex'] = True

    im_e, fmaps_e = testplot_p4(r=0)
    im_r, fmaps_r = testplot_p4(r=1)

    plot_p4(fmaps_e, fontsize=10, labelpad_factor_1=.3, labelpad_factor_2=.6, figsize=(1.6, 1.6))
    plt.savefig('./p4_fmap_e_mini.eps', format='eps', dpi=600)
    plot_p4(fmaps_r, fontsize=10, labelpad_factor_1=.3, labelpad_factor_2=.6, figsize=(1.6, 1.6))
    plt.savefig('./p4_fmap_r_mini.eps', format='eps', dpi=600)


def testplot_p4(im=None, r=0):
    if im is None:
        # im = np.zeros((39, 39), dtype='float32')
        # im[10:30, 14:16] = 1.
        # im[10:12, 14:30] = 1.
        # im[18:20, 14:24] = 1.
        # im = gaussian_filter(im, sigma=1., mode='constant', cval=0.0)
        im = np.zeros((5, 5), dtype='float32')
        im[0:5, 1] = 1.
        im[0, 1:4] = 1.
        im[2, 1:3] = 1.

    # from gfunc.OLD.transform_Z2_func import rotate_z2_func
    from groupy.gfunc.z2func_array import Z2FuncArray
    from groupy.garray.C4_array import C4Array
    def rotate_z2_func(im, r):
        imf = Z2FuncArray(im)
        rot = C4Array([r], 'int')
        rot_imf = rot * imf
        return rot_imf.v

    im = rotate_z2_func(im, r)

    # im = lena()
    # filter = np.array([1, 2, 1])[:, None] * np.array([-1, 0, 1.])[None, :]

    filter1 = np.array([[-1., 0., 1.],
                        [-2., 0., 2.],
                        [-1., 0., 1.]]).astype(np.float32)
    filter2 = rotate_z2_func(filter1, 1)
    filter3 = rotate_z2_func(filter1, 2)
    filter4 = rotate_z2_func(filter1, 3)

    # imf1 = correlate2d(im, filter1, 'valid')
    # imf2 = correlate2d(im, filter2, 'valid')
    # imf3 = correlate2d(im, filter3, 'valid')
    # imf4 = correlate2d(im, filter4, 'valid')
    # imf1 = convolve2d(im, filter1, 'valid')
    # imf2 = convolve2d(im, filter2, 'valid')
    # imf3 = convolve2d(im, filter3, 'valid')
    # imf4 = convolve2d(im, filter4, 'valid')

    from chainer.functions import Convolution2D
    from chainer import Variable
    im = im.astype(np.float32)
    pad = 2
    imf1 = Convolution2D(in_channels=1, out_channels=1, ksize=3, bias=0., pad=pad, initialW=filter1)(
        Variable(im[None, None])).data[0, 0]
    imf2 = Convolution2D(in_channels=1, out_channels=1, ksize=3, bias=0., pad=pad, initialW=filter2)(
        Variable(im[None, None])).data[0, 0]
    imf3 = Convolution2D(in_channels=1, out_channels=1, ksize=3, bias=0., pad=pad, initialW=filter3)(
        Variable(im[None, None])).data[0, 0]
    imf4 = Convolution2D(in_channels=1, out_channels=1, ksize=3, bias=0., pad=pad, initialW=filter4)(
        Variable(im[None, None])).data[0, 0]

    return im, np.r_[[imf1, imf2, imf3, imf4]]


def paper_plots_p4m():
    import matplotlib
    matplotlib.rcParams['ps.useafm'] = True
    matplotlib.rcParams['pdf.use14corefonts'] = True
    matplotlib.rcParams['text.usetex'] = True

    im_e, fmaps_e = testplot_p4m(m=0, r=0)
    im_r, fmaps_r = testplot_p4m(m=0, r=1)
    im_m, fmaps_m = testplot_p4m(m=1, r=0)

    plot_p4m(fmaps_e.reshape(2, 4, 7, 7), rlabels='cayley2', fontsize=10, labelpad_factor_1=0.2,
             labelpad_factor_2=0.8, labelpad_factor_3=0.5, labelpad_factor_4=1.2,
             figsize=(2.5, 2.5), rcolor='red', mcolor='blue')
    plt.savefig('./p4m_fmap_e_mini.eps', format='eps', dpi=600)
    plot_p4m(fmaps_r.reshape(2, 4, 7, 7), rlabels='cayley2', fontsize=10, labelpad_factor_1=0.2,
             labelpad_factor_2=0.8, labelpad_factor_3=0.5, labelpad_factor_4=1.2,
             figsize=(2.5, 2.5), rcolor='red', mcolor='blue')
    plt.savefig('./p4m_fmap_r_mini.eps', format='eps', dpi=600)
    plot_p4m(fmaps_m.reshape(2, 4, 7, 7), rlabels='cayley2', fontsize=10, labelpad_factor_1=0.2,
             labelpad_factor_2=0.8, labelpad_factor_3=0.5, labelpad_factor_4=1.2,
             figsize=(2.5, 2.5), rcolor='red', mcolor='blue')
    plt.savefig('./p4m_fmap_m_mini.eps', format='eps', dpi=600)


def testplot_p4m(im=None, m=0, r=0):

    if im is None:
        # im = np.zeros((39, 39), dtype='float32')
        # im[10:30, 14:16] = 1.
        # im[10:12, 14:30] = 1.
        # im[18:20, 14:24] = 1.
        # im = gaussian_filter(im, sigma=1., mode='constant', cval=0.0)
        im = np.zeros((5, 5), dtype='float32')
        im[0:5, 1] = 1.
        im[0, 1:4] = 1.
        im[2, 1:3] = 1.
        # im = gaussian_filter(im, sigma=1., mode='constant', cval=0.0)

    # from gfunc.OLD.transform_Z2_func import rotate_flip_z2_func
    from groupy.gfunc.z2func_array import Z2FuncArray
    from groupy.garray.D4_array import D4Array
    def rotate_flip_z2_func(im, flip, theta_index):
        imf = Z2FuncArray(im)
        rot = D4Array([flip, theta_index], 'int')
        rot_imf = rot * imf
        return rot_imf.v
    im = rotate_flip_z2_func(im, m, r)

    # im = lena()
    # filter = np.array([1, 2, 1])[:, None] * np.array([-1, 0, 1.])[None, :]

    filter_e = np.array([[-1., -4., 1.],
                         [-2., 0., 2.],
                         [-1., 0., 1.]])
    # filter_e = np.array([[0, 1, 0, -1, 0],
    #                     [0, 1, 0, -1, 0],
    #                     [0, 0, 0, 0, 0],
    #                     [0, -1, 0, 1, 0],
    #                     [1, -1, 3, 1, -1.]])
    filter_r1 = rotate_flip_z2_func(filter_e, flip=0, theta_index=1)
    filter_r2 = rotate_flip_z2_func(filter_e, flip=0, theta_index=2)
    filter_r3 = rotate_flip_z2_func(filter_e, flip=0, theta_index=3)

    filter_m = rotate_flip_z2_func(filter_e, flip=1, theta_index=0)
    filter_mr1 = rotate_flip_z2_func(filter_e, flip=1, theta_index=1)
    filter_mr2 = rotate_flip_z2_func(filter_e, flip=1, theta_index=2)
    filter_mr3 = rotate_flip_z2_func(filter_e, flip=1, theta_index=3)

    print filter_e
    print filter_r1
    print filter_r2
    print filter_r3
    print filter_m
    print filter_mr1
    print filter_mr2
    print filter_mr3

    # filter_e = filter_e[::-1, ::-1]
    # filter_r1 = filter_r1[::-1, ::-1]
    # filter_r2 = filter_r2[::-1, ::-1]
    # filter_r3 = filter_r3[::-1, ::-1]
    # filter_m = filter_m[::-1, ::-1]
    # filter_mr1 = filter_mr1[::-1, ::-1]
    # filter_mr2 = filter_mr2[::-1, ::-1]
    # filter_mr3 = filter_mr3[::-1, ::-1]

    # imf_e = correlate2d(im, filter_e, 'valid')
    # imf_r1 = correlate2d(im, filter_r1, 'valid')
    # imf_r2 = correlate2d(im, filter_r2, 'valid')
    # imf_r3 = correlate2d(im, filter_r3, 'valid')
    # imf_m = correlate2d(im, filter_m, 'valid')
    # imf_mr1 = correlate2d(im, filter_mr1, 'valid')
    # imf_mr2 = correlate2d(im, filter_mr2, 'valid')
    # imf_mr3 = correlate2d(im, filter_mr3, 'valid')

    from chainer.functions import Convolution2D
    from chainer import Variable
    im = im.astype(np.float32)
    ksize = filter_e.shape[0]
    imf_e = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2,initialW=filter_e)(Variable(im[None, None])).data[0, 0]
    imf_r1 = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_r1)(Variable(im[None, None])).data[0, 0]
    imf_r2 = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_r2)(Variable(im[None, None])).data[0, 0]
    imf_r3 = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_r3)(Variable(im[None, None])).data[0, 0]
    imf_m = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_m)(Variable(im[None, None])).data[0, 0]
    imf_mr1 = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_mr1)(Variable(im[None, None])).data[0, 0]
    imf_mr2 = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_mr2)(Variable(im[None, None])).data[0, 0]
    imf_mr3 = Convolution2D(in_channels=1, out_channels=1, ksize=ksize, bias=0., pad=2, initialW=filter_mr3)(Variable(im[None, None])).data[0, 0]

    return im, np.r_[[imf_e, imf_r1, imf_r2, imf_r3, imf_m, imf_mr1, imf_mr2, imf_mr3]]
